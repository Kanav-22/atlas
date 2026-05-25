# Atlas — AI Travel Intelligence Agent

Ask anything about travel in plain English. Atlas finds real flights, hotels, and live weather using an agentic AI pipeline.

**Live Demo:** https://atlas-smoky-omega.vercel.app

---

## What it does

Atlas is a full-stack AI travel assistant. Type a question like "Find me flights from Delhi to Mumbai on June 15" or "Hotels in Goa from June 20 to 25" — the AI agent understands your intent, calls the right data sources, and responds in natural language.

---

## Tech Stack

**Backend:** Python, FastAPI, Groq API (Llama 3.3 70B), LLM Function Calling, Sky Scrapper API, OpenWeatherMap API

**Frontend:** Next.js, React, Tailwind CSS

**Deployment:** Backend on Render, Frontend on Vercel

---

## Key Features

- Agentic AI routing — LLM decides which API to call based on user intent
- Real-time data — live flight prices, hotel availability, weather forecasts
- Natural language interface — no forms, just conversation
- Multi-tool support — flights, hotels, weather in one chat

---

## Architecture

User sends a plain English query → Next.js frontend → FastAPI backend → Groq LLM agent decides which tool to call → Sky Scrapper API (flights/hotels) or OpenWeatherMap (weather) → natural language response back to user

---

## Local Setup

Clone the repo, then:

Backend:
    cd backend
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    Create .env with your API keys
    uvicorn main:app --reload

Frontend:
    cd frontend
    npm install
    Create .env.local with NEXT_PUBLIC_API_URL
    npm run dev

---

## Environment Variables

Backend .env:
    RAPIDAPI_KEY=your_key
    RAPIDAPI_HOST=sky-scrapper.p.rapidapi.com
    GROQ_API_KEY=your_key
    OPENWEATHER_KEY=your_key
    AVIATIONSTACK_KEY=your_key

Frontend .env.local:
    NEXT_PUBLIC_API_URL=http://127.0.0.1:8000