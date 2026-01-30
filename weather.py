# pip3 install requests
from api import api
import requests

# API_KEY = "d2e91e86245680dc0c39ed169d6b226b"
API_KEY = api()

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("City not found!")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

def main():
    while True:
        city = input("\nEnter city name (or 'exit'): ")

        if city.lower() == "exit":
            break

        get_weather(city)

if __name__ == "__main__":
    main()
