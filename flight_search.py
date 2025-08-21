import os
import requests
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

CITY_TO_IATA = {
    "New York": "JFK",
    "Los Angeles": "LAX",
    "San Francisco": "SFO",
    "London": "LON"
}

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        return CITY_TO_IATA.get(city_name.strip(), "")

    def get_cheapest_flight(self, origin_code, destination_code, from_date, to_date, is_direct=True):
        # Simulated response to avoid Amadeus 500 error
        print(f"Simulating flight for {origin_code} → {destination_code}")
        return FlightData(
            price="199.99",
            origin_city=origin_code,
            origin_airport=origin_code,
            destination_city=destination_code,
            destination_airport=destination_code,
            out_date=from_date,
            return_date=to_date,
            stops=0
        )
