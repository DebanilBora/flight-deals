✈️ Flight Deals Finder

A Python automation project that searches for cheap flights and notifies subscribed users via SMS and email when prices drop below a set threshold.

This project integrates with:

Amadeus / Tequila API (for flight search)

Sheety API (to manage destinations & customer data in Google Sheets)

Twilio (for SMS alerts)

SMTP (for email notifications)

🚀 Features

Fetches destination cities and price thresholds from Google Sheets.

Automatically updates missing IATA airport codes.

Searches for cheap flights from your origin city.

Sends SMS alerts using Twilio.

Sends email notifications to all subscribed customers.

Detects flights within the next 90 days.

Includes stopover information if applicable.

🛠️ Tech Stack

Python 3

requests for API communication

smtplib for email notifications

Twilio API for SMS

Sheety API for Google Sheets integration

Amadeus/Tequila API for flight data

📂 Project Structure

.
├── main.py                # Main script (your provided code)
├── data_manager.py        # Handles Google Sheets data (via Sheety API)
├── flight_search.py       # Handles flight search API requests
├── flight_data.py         # Defines FlightData class to structure flight info
├── notification_manager.py# Manages SMS/email notifications
├── requirements.txt       # Python dependencies
├── .env                   # API keys & credentials


⚙️ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/DebanilBora/flight-deals.git
cd flight-deals-finder

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create a .env file

Add your credentials:

TEQUILA_API_KEY=your_amadeus_or_tequila_api_key
SHEET_ENDPOINT=your_google_sheety_endpoint
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=+123456789
TWILIO_TO_NUMBER=+987654321
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password

4️⃣ Run the script
python main.py

📊 Google Sheet Structure

Flight Prices Sheet

city	iataCode	lowestPrice
Paris	PAR	300
Berlin	BER	250
Tokyo	TYO	600

Customer Emails Sheet

firstName	lastName	email
John	Doe	john@example.com

Alice	Smith	alice@example.com
📩 Notifications

SMS Example:

Low price alert! Only GBP199 to fly from JFK to CDG.
Departure: 2025-09-12, Return: 2025-09-26.
This flight has 1 stop.


Email Example:
Subject: ✈️ New Flight Deal!
Body: Same as SMS message.

🏷️ Tags

python automation api flight-search twilio smtp sheety google-sheets
