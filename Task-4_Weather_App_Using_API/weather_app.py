import requests

API_KEY = "your_openweathermap_api_key"  # Replace with your actual key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data = response.json()
        if data.get("cod") != 200:
            print("City not found.")
            return
        print(f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)