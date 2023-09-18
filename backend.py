import requests

def get_data(place, forecastdays, kind):

    APIkey = 'b0262bf4ebad231dd829d5ff62348f0e' 
    
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'   
    response = requests.get(url)
    data = response.json()
    nrobs = 8*forecastdays
    filtered_data = data['list']
    filtered_data = filtered_data[:nrobs]

    if kind == 'Temperature':
        filtered_data= [temps['main']['temp'] for temps in filtered_data]

    if kind == 'Sky':
        filtered_data = [sky['weather'][0]['main'] for sky in filtered_data]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place = 'Pune', forecastdays=2, kind='Sky'))

