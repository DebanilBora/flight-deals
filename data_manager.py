import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheet_endpoint = os.getenv("SHEET_ENDPOINT")
        self.users_endpoint = os.getenv("USERS_ENDPOINT")
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(self.sheet_endpoint, auth=(self.username, self.password))
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{self.sheet_endpoint}/{city['id']}",
                json=new_data,
                auth=(self.username, self.password)
            )

    def get_customer_emails(self):
        response = requests.get(self.users_endpoint, auth=(self.username, self.password))
        response.raise_for_status()
        return response.json()["user"]
