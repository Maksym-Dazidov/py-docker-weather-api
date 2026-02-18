import requests
import os
from dotenv import load_dotenv
load_dotenv()
def get_weather(city:str) -> None:
    api_key = os.getenv("API_KEY")
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data["current"]["temp_c"])
    print(data["current"]["condition"]["text"])



if __name__ == "__main__":
    get_weather("Paris")
