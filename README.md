# Weather CLI App 🌤️

A simple weather application that fetches real-time weather data using the OpenWeatherMap API. Available as both a command-line interface and a web app using Streamlit.

## Features

- 🌡️ Current temperature in Celsius
- 💧 Humidity percentage
- ☁️ Weather description
- 🏙️ City and country information
- 💻 Command-line interface
- 🌐 Web interface with Streamlit

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

### Option 1: Command Line Interface
```bash
python weather_app.py
```
The app will prompt you to enter a city name.

### Option 2: Web Interface (Streamlit)
```bash
streamlit run streamlit_app.py
```
This will open a web browser with an interactive interface where you can enter city names and see the weather data displayed with metrics and formatting.

## Example Outputs

### CLI Output
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
- `streamlit` library
- OpenWeatherMap API key

## License

This project is open source and available under the MIT License.
