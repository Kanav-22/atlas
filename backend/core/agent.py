import os
import json
from groq import Groq
from dotenv import load_dotenv
from core.flight_service import search_flights
from core.hotel_service import search_hotels
from core.weather_service import get_weather

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_flights",
            "description": "Search for flights between two cities on a specific date",
            "parameters": {
                "type": "object",
                "properties": {
                    "origin_city": {"type": "string", "description": "Departure city e.g. Delhi"},
                    "destination_city": {"type": "string", "description": "Arrival city e.g. Mumbai"},
                    "date": {"type": "string", "description": "Travel date in YYYY-MM-DD format"},
                    "adults": {"type": "integer", "description": "Number of adult passengers", "default": 1}
                },
                "required": ["origin_city", "destination_city", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_hotels",
            "description": "Search for hotels in a city for specific dates",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City to search hotels in"},
                    "checkin": {"type": "string", "description": "Check-in date in YYYY-MM-DD format"},
                    "checkout": {"type": "string", "description": "Check-out date in YYYY-MM-DD format"},
                    "adults": {"type": "integer", "description": "Number of guests", "default": 1}
                },
                "required": ["city", "checkin", "checkout"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather forecast for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"]
            }
        }
    }
]

def run_tool(tool_name: str, tool_args: dict):
    if tool_name == "search_flights":
        return search_flights(**tool_args)
    elif tool_name == "search_hotels":
        return search_hotels(**tool_args)
    elif tool_name == "get_weather":
        return get_weather(**tool_args)
    else:
        return {"error": f"Unknown tool: {tool_name}"}

def chat(user_message: str, conversation_history: list = []):
    messages = [
        {
            "role": "system",
            "content": """You are Atlas, an intelligent travel assistant. 
You help users find flights, hotels, and weather information.
When users ask travel questions, use the available tools to get real data.
Always respond in a friendly, helpful tone.
When presenting flight or hotel results, format them clearly.
Today's date context: use 2026 for any relative date references."""
        }
    ] + conversation_history + [
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        max_tokens=1000
    )

    response_message = response.choices[0].message

    if response_message.tool_calls:
        messages.append(response_message)

        for tool_call in response_message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            print(f"Agent calling: {tool_name} with {tool_args}")

            result = run_tool(tool_name, tool_args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1000
        )

        return final_response.choices[0].message.content

    return response_message.content