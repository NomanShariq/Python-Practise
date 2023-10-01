import os
from dotenv import load_dotenv
import requests
from pprint import pprint


load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather ***\n')
    
    city = input('\nPlease Enter you city:\n')
    
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    # print(weather_data)
    
    pprint(weather_data)
    
    print(f'\nThe Weather city name: {weather_data["name"]}')
    print(f'\nThe temp of city: {weather_data["main"]["temp"]}')
    print(f'\nThe feels like: {weather_data["main"]["feels_like"]}')
    print(f'\nThe condition of city: {weather_data["weather"][0]["description"]}')
    
if __name__ == "__main__":    
    get_current_weather()