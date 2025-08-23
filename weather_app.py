#!/usr/bin/env python3
"""
Weather CLI App
"""

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
        'units': 'imperial'
    }
    
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    """Display formatted weather information"""

    temp_celsius = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description'].title()
    
    city_name = weather_data['name']
    country = weather_data['sys']['country']
    
    # Display weather report
    print("\n" + "="*50)
    print(f"🌤️  WEATHER REPORT FOR {city_name.upper()}, {country}")
    print("="*50)
    print(f"🌡️  Temperature: {temp_celsius}°F")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️  Description: {description}")
    print("="*50)

def main():
    """Main application function"""
    print("🌤️  Welcome to Weather CLI App!")
    
    city = input("🏙️  Enter a city name: ").strip()
    
    print(f"🔍 Fetching weather data for {city}...")
    
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()