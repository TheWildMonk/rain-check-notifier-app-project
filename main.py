import requests

# Constants
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6bd6ded191e85182ba748e6b16967fa5"

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

# for each_hour in range(13):
weather_codes = [weather_data["hourly"][each_hour]["weather"][0]["id"] for each_hour in range(13)]
if any(weather_code < 600 for weather_code in weather_codes):
    print("Bring an umbrella!")
