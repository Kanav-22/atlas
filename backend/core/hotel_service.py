import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")
MOCK_MODE = True

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": RAPIDAPI_HOST
}

def search_hotels(city: str, checkin: str, checkout: str, adults: int = 1):
    if MOCK_MODE:
        return {
            "city": city,
            "checkin": checkin,
            "checkout": checkout,
            "hotels": [
                {"name": "Sahara Star", "stars": 5, "rating": 8.9, "price_per_night": "₹8,200"},
                {"name": "ITC Maratha", "stars": 5, "rating": 9.1, "price_per_night": "₹12,500"},
                {"name": "Novotel", "stars": 4, "rating": 8.2, "price_per_night": "₹5,800"},
                {"name": "Hotel Kohinoor", "stars": 3, "rating": 7.5, "price_per_night": "₹2,900"},
                {"name": "Ibis", "stars": 3, "rating": 7.8, "price_per_night": "₹2,400"}
            ]
        }

    url = "https://sky-scrapper.p.rapidapi.com/api/v1/hotels/searchDestinationOrHotel"
    params = {"query": city}
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    if not data.get("data"):
        return {"error": f"Could not find location: {city}"}

    first = data["data"][0]
    entity_id = first["entityId"]
    city_name = first["entityName"]

    url2 = "https://sky-scrapper.p.rapidapi.com/api/v1/hotels/searchHotels"
    params2 = {
        "entityId": entity_id,
        "checkin": checkin,
        "checkout": checkout,
        "adults": adults,
        "rooms": 1
    }
    response2 = requests.get(url2, headers=HEADERS, params=params2)
    data2 = response2.json()
    if not data2.get("data"):
        return {"error": "No hotels found"}

    hotels_list = data2["data"].get("hotels", [])
    hotels = []
    for hotel in hotels_list[:5]:
        price_raw = hotel.get("price", "N/A")
        price = price_raw.get("lead", {}).get("formatted", "N/A") if isinstance(price_raw, dict) else str(price_raw)
        hotels.append({
            "name": hotel.get("name", "Unknown"),
            "stars": hotel.get("stars", "N/A"),
            "rating": hotel.get("reviewsSummary", {}).get("score", "N/A") if isinstance(hotel.get("reviewsSummary"), dict) else "N/A",
            "price_per_night": price
        })
    return {"city": city_name, "checkin": checkin, "checkout": checkout, "hotels": hotels}