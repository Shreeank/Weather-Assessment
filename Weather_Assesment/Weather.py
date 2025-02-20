import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "3027ee0d52bcbee506dfdb8d4bbaf44b"

cities = ["New York", "London", "Tokyo", "Mumbai", "Sydney"]

# Empty list to store weather data
weather_data = []

def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        return {"City": city, "Temperature": temp, "Weather": weather, "Humidity": humidity}
    else:
        print(f"Weather data for {city} not found.")
        return None

for city in cities:
    result = fetch_weather(city)
    if result:
        weather_data.append(result)

df = pd.DataFrame(weather_data)

print("\nWeather Data:")
print(df)

plt.figure(figsize=(8, 5))
plt.bar(df["City"], df["Temperature"], color="skyblue")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperature in Different Cities")
plt.show()

max_temp_city = df.loc[df["Temperature"].idxmax()]
min_temp_city = df.loc[df["Temperature"].idxmin()]

print(f"\nHottest City: {max_temp_city['City']} with {max_temp_city['Temperature']}°C")
print(f"Coldest City: {min_temp_city['City']} with {min_temp_city['Temperature']}°C")
