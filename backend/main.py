from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.flights import router as flights_router
from routes.weather import router as weather_router
from routes.hotels import router as hotels_router
from routes.chat import router as chat_router

app = FastAPI(title="Atlas Travel API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flights_router, prefix="/api")
app.include_router(weather_router, prefix="/api")
app.include_router(hotels_router, prefix="/api")
app.include_router(chat_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Atlas API is running"}