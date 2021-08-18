import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Constants
load_dotenv("/Volumes/Workstation/Learning Center/Data Science/"
            "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.getenv("OWM_API_KEY")
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NO = "+18503184267"
RECEIVER = "+8801701340839"

weather_params = {
    "lat": 23.7104,
    "lon": 90.4074,
    "exclude": "current,daily,minutely,alerts",
    "appid": API_KEY,
}

# Connection to OpenWeather API
connection = requests.get(OWM_ENDPOINT, params=weather_params)
connection.raise_for_status()
weather_data = connection.json()

# Create list of weather codes for next 12 hours
hours = weather_data["hourly"][:12]
weather_codes = [each_hour["weather"][0]["id"] for each_hour in hours]

# Check rain code from weather_codes
if any(weather_code < 600 for weather_code in weather_codes):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️ when you go out.",
            from_=TWILIO_PHONE_NO,
            to=RECEIVER
        )

    print(message.status)
