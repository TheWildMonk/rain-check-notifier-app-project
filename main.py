import requests
from twilio.rest import Client

# Constants
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "{Open Weather API Ke}y"
ACCOUNT_SID = "{Twilio Account SID}"
AUTH_TOKEN = "{Twilio Account AUTH Token}"
TWILIO_PHONE_NO = "{Twilio Phone No.}"
RECEIVER = "{Receiver's Phone No.}"

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

hours = weather_data["hourly"][:12]
weather_codes = [each_hour["weather"][0]["id"] for each_hour in hours]
if any(weather_code < 600 for weather_code in weather_codes):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️ when you go out.",
            from_=TWILLIO_PHONE_NO,
            to=RECEIVER
        )

    print(message.status)
