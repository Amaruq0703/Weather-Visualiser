import requests

def get_data(place, forecastdays=None, time=None):

    APIkey = 'b0262bf4ebad231dd829d5ff62348f0e' 
    
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'
    
    response = requests.get(url)

    data = response.json()

    return data

if __name__ == '__main__':
    print(get_data(place = 'Pune'))

