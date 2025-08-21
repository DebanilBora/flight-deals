# ✈️ Flight Deals Tracker

A Python project that finds cheap flight deals and notifies subscribed users via **SMS** and **Email**.  
This project is based on the Flight Deals Capstone from Angela Yu's *100 Days of Code: Python Bootcamp*.

---

## 🚀 Features
- Fetches flight data using the **Amadeus API** (or Tequila/Kiwi API, depending on your setup).
- Checks flights from an origin city (e.g., `JFK`) to multiple destinations.
- Compares prices against the lowest price stored in Google Sheets.
- Sends **SMS alerts** (via Twilio).
- Sends **Email alerts** (via SMTP/Gmail).
- Manages destination and customer data using **Sheety API** + Google Sheets.

---

## 📂 Project Structure
flight-deals/
│── main.py # Main script to run the flight deals checker
│── data_manager.py # Handles data retrieval & update with Sheety API
│── flight_search.py # Handles flight search API integration
│── notification_manager.py # Sends SMS and Email alerts
│── flight_data.py # Flight data model
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── .gitignore # Ignored files


---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DebanilBora/flight-deals.git
   cd flight-deals


Create a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the root folder and add the following:

# Sheety API
SHEETY_PRICES_ENDPOINT="https://api.sheety.co/xxxxxx/flightDeals/prices"
SHEETY_USERS_ENDPOINT="https://api.sheety.co/xxxxxx/flightDeals/users"

# Flight API (Amadeus or Tequila/Kiwi)
AMADEUS_API_KEY="your_amadeus_api_key"
AMADEUS_API_SECRET="your_amadeus_api_secret"

# Twilio API
TWILIO_SID="your_twilio_sid"
TWILIO_AUTH_TOKEN="your_twilio_auth_token"
TWILIO_FROM_NUMBER="+1234567890"

# Email (SMTP - Gmail)
EMAIL="your_email@gmail.com"
EMAIL_PASSWORD="your_app_password"  # Gmail App Password, not regular password


⚠️ Do NOT commit this .env file to GitHub.

▶️ Running the Project
python main.py


If a cheaper flight is found:

An SMS alert will be sent via Twilio.

An Email alert will be sent to all subscribed customers.

📧 Notes on Gmail SMTP

Google no longer allows normal passwords for SMTP.

Enable 2-Step Verification in your Google account.

Generate an App Password for Gmail and use that in .env.

✅ Example Notification
Subject: Flight Deal Alert!
Low price alert! Only GBP150 to fly from JFK to CDG.
Departure: 2025-09-15, Return: 2025-09-25. This flight has 1 stop.
