# Weather CLI App 🌤️

A simple command-line weather application that fetches real-time weather data using the OpenWeatherMap API.

## Features

- 🌡️ Current temperature in Celsius
- 💧 Humidity percentage
- ☁️ Weather description
- 🏙️ City and country information

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jonas-duke/weather-cli-app
cd weather-cli-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get an API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/)
2. Sign up for a free account
3. Go to API keys section and copy your key

### 4. Configure Environment
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your API key:
   ```
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```

## Usage

### Interactive Mode
```bash
python weather_app.py
```
The app will prompt you to enter a city name.

## Example Output

```
🌤️  Welcome to Weather CLI App!
🔍 Fetching weather data for Miami...

==================================================
🌤️  WEATHER REPORT FOR MIAMI, US
==================================================
🌡️  Temperature: 28.5°C
💧 Humidity: 78%
☁️  Description: Partly Cloudy
==================================================
```

## Requirements

- Python 3.6+
- `requests` library
- `python-dotenv` library
- OpenWeatherMap API key

## License

This project is open source and available under the MIT License.
