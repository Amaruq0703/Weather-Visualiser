import requests


def get_data(place, forecastdays): 
    APIkey = 'b0262bf4ebad231dd829d5ff62348f0e'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'   
    response = requests.get(url)
    data = response.json()
    nrobs = 8*forecastdays
    filtered_data = data['list']
    filtered_data = filtered_data[:nrobs]

    return filtered_data



