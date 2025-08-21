from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "JFK"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

# Only fetch IATA codes if they are missing
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
THREE_MONTHS = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")

customer_data = data_manager.get_customer_emails()
emails = [user["email"] for user in customer_data if "email" in user]

for destination in sheet_data:
    destination["iataCode"] = destination["iataCode"].strip()
    flight = flight_search.get_cheapest_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        TOMORROW,
        THREE_MONTHS
    )

    if flight and float(flight.price) < destination["lowestPrice"]:
        message = (
            f"Low price alert! Only GBP{flight.price} to fly from {flight.origin_airport} to {flight.destination_airport}.\n"
            f"Departure: {flight.out_date}, Return: {flight.return_date}."
        )
        if flight.stops > 0:
            message += f" This flight has {flight.stops} stop(s)."

        notification_manager.send_sms(message)
        notification_manager.send_emails(emails, message)
    elif not flight:
        print(f"No flights found for {destination['city']}")
