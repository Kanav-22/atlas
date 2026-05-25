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

def search_airport(query: str):
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"
    params = {"query": query, "locale": "en-US"}
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    if not data.get("data"):
        return None
    first = data["data"][0]
    flight_params = first["navigation"]["relevantFlightParams"]
    return {
        "skyId": flight_params["skyId"],
        "entityId": flight_params["entityId"],
        "name": first["presentation"]["title"],
        "city": first["presentation"]["suggestionTitle"]
    }

def search_flights(origin_city: str, destination_city: str, date: str, adults: int = 1):
    if MOCK_MODE:
        return {
            "origin": origin_city,
            "destination": destination_city,
            "date": date,
            "flights": [
                {"airline": "IndiGo", "departure": "06:00", "arrival": "08:10", "duration": "2h 10m", "stops": 0, "price": "₹4,823"},
                {"airline": "Air India", "departure": "09:30", "arrival": "11:45", "duration": "2h 15m", "stops": 0, "price": "₹5,240"},
                {"airline": "SpiceJet", "departure": "14:00", "arrival": "16:20", "duration": "2h 20m", "stops": 0, "price": "₹3,999"},
                {"airline": "Akasa Air", "departure": "18:30", "arrival": "20:45", "duration": "2h 15m", "stops": 0, "price": "₹4,450"},
                {"airline": "Vistara", "departure": "21:00", "arrival": "23:10", "duration": "2h 10m", "stops": 0, "price": "₹6,100"}
            ]
        }

    origin = search_airport(origin_city)
    destination = search_airport(destination_city)
    if not origin or not destination:
        return {"error": "Could not find airports for given cities"}

    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"
    params = {
        "originSkyId": origin["skyId"],
        "destinationSkyId": destination["skyId"],
        "originEntityId": origin["entityId"],
        "destinationEntityId": destination["entityId"],
        "date": date,
        "adults": adults,
        "currency": "INR",
        "locale": "en-US",
        "market": "IN",
        "countryCode": "IN"
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    if not data.get("data"):
        return {"error": "No flights found"}

    itineraries = data["data"].get("itineraries", [])
    flights = []
    for item in itineraries[:5]:
        legs = item.get("legs", [])
        if not legs:
            continue
        leg = legs[0]
        flights.append({
            "airline": leg["carriers"]["marketing"][0]["name"],
            "departure": leg["departure"],
            "arrival": leg["arrival"],
            "duration": f"{leg['durationInMinutes'] // 60}h {leg['durationInMinutes'] % 60}m",
            "stops": len(leg["segments"]) - 1,
            "price": item["price"]["formatted"],
            "origin": origin["city"],
            "destination": destination["city"]
        })
    return {"origin": origin["city"], "destination": destination["city"], "date": date, "flights": flights}