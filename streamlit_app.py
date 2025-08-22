import streamlit as st
import os
import requests
from dotenv import load_dotenv

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API"""
    load_dotenv()
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }
    
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    """Display weather information in Streamlit"""
    # Extract required data
    temp_celsius = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description'].title()
    
    # Additional data for enhanced display
    city_name = weather_data['name']
    country = weather_data['sys']['country']
    
    # Display in Streamlit
    st.subheader(f"🌤️ Weather in {city_name}, {country}")
    st.metric("🌡️ Temperature", f"{temp_celsius}°C")
    st.metric("💧 Humidity", f"{humidity}%")
    st.write(f"**☁️ Description:** {description}")

# Streamlit UI
st.title("🌤️ Weather App")
city = st.text_input("🏙️ Enter a city name:")

if city:
    weather_data = get_weather(city)
    display_weather(weather_data)