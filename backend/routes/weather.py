from fastapi import APIRouter
from core.weather_service import get_weather

router = APIRouter()

@router.get("/weather")
def weather(city: str):
    return get_weather(city)