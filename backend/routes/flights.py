from fastapi import APIRouter
from core.flight_service import search_flights

router = APIRouter()

@router.get("/flights/search")
def flight_search(origin: str, destination: str, date: str, adults: int = 1):
    result = search_flights(origin, destination, date, adults)
    return result