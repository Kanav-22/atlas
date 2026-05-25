import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_KEY = os.getenv("OPENWEATHER_KEY")

def get_weather(city: str):
    """Get current weather + 5 day forecast for a city"""
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": WEATHER_KEY,
        "units": "metric",
        "cnt": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("cod") != "200":
        return {"error": f"Could not get weather for {city}"}

    forecasts = []
    for item in data["list"]:
        forecasts.append({
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "feels_like": item["main"]["feels_like"],
            "description": item["weather"][0]["description"],
            "humidity": item["main"]["humidity"],
            "wind_speed": item["wind"]["speed"]
        })

    return {
        "city": data["city"]["name"],
        "country": data["city"]["country"],
        "forecasts": forecasts
    }