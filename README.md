# Atlas — AI Travel Intelligence Agent

Ask anything about travel in plain English. Atlas finds real flights, hotels, and live weather using an agentic AI pipeline.

**Live Demo:** https://atlas-smoky-omega.vercel.app

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

---

## Architecture

User query  Next.js frontend  FastAPI backend  Groq LLM agent  Sky Scrapper API (flights/hotels) or OpenWeatherMap (weather)  natural language response

---

## Local Setup

Backend: cd backend, pip install -r requirements.txt, uvicorn main:app --reload

Frontend: cd frontend, npm install, npm run dev
