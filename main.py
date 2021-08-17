import requests
from twilio.rest import Client

# Constants
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6bd6ded191e85182ba748e6b16967fa5"
ACCOUNT_SID = "ACf54a9c5f5c62fd561e2f5ccfd18aa36a"
AUTH_TOKEN = "5dea37ebedea366f69b0d481b5434df2"
TWILLIO_PHONE_NO = "+18503184267"
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
