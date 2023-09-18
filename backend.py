import requests
from config import APIkey

def get_data(place, forecastdays): 
    
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'   
    response = requests.get(url)
    data = response.json()
    nrobs = 8*forecastdays
    filtered_data = data['list']
    filtered_data = filtered_data[:nrobs]

    return filtered_data



