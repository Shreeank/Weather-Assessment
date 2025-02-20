# Weather-Assessment 🌦️

This project retrieves real-time weather data for multiple cities using the OpenWeatherMap API, stores the data in a Pandas DataFrame, visualizes temperatures using Matplotlib, and identifies the hottest and coldest cities.

## Features
- Fetches current weather details (temperature, humidity, weather description) for multiple cities.
- Stores the data in a CSV file.
- Generates a bar chart to visualize temperature differences.
- Identifies the city with the highest and lowest temperatures.

## Technologies Used
- Python 🐍
- OpenWeatherMap API 🌍
- Pandas 📊
- Matplotlib 📈
- Requests 📡

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/weather-data-analysis.git
   cd weather-data-analysis
2.Install dependencies:
  pip install -r requirements.txt

3.Replace your_api_key_here in weather_script.py with your actual OpenWeatherMap API key.

4.Run the script:
  python weather_script.py

5.The script will:
  •Display weather data.
  •Save data to weather_data.csv.
  •Show a bar chart comparing temperatures.
