import pandas as pd
import requests

def global_weather(city_name,laitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={laitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    raw_data = response.json()

    current_weather = raw_data["current_weather"]

    windspeed = current_weather["windspeed"]
    temperature = current_weather["temperature"]
    weather_code = current_weather["weathercode"]

    return {
        "City": city_name,
        "Temperature": temperature,
        "Windspeed": windspeed,
        "Weathercode": weather_code
    }

cities = [

    ("Hyderabad",17.38,78.47),
    ("Delhi",28.61,77.20),
    ("Bangalore", 12.97, 77.59),
    ("Chennai", 13.08, 80.27),
    ("Kolkata", 22.57, 88.36),
    ("Mumbai", 19.72, 72.87),
    ("Pune", 18.52, 73.85),
    ("Jaipur", 26.91, 75.78),
    ("Ahmedabad", 23.02, 72.57),
    ("Lucknow", 26.84, 80.94)

    ]
    

all_weather_data = []

for city in cities:
    city_name = city[0]
    latitude = city[1]
    longitude = city[2]

    weather = global_weather(city_name,latitude,longitude)
    all_weather_data.append(weather)

df = pd.DataFrame(all_weather_data)
print(df)

df.to_csv("India_Weather_Data.csv", index=False)
print(" ")
print("✅ Data successfully saved as CSV file!")
print("📈 Check Dashboard in Power BI!")