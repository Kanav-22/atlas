from fastapi import APIRouter
from core.hotel_service import search_hotels

router = APIRouter()

@router.get("/hotels/search")
def hotel_search(city: str, checkin: str, checkout: str, adults: int = 1):
    return search_hotels(city, checkin, checkout, adults)