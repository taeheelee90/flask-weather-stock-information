import requests

def get_weather_info(city):
    # SET VARIABLE
    API_KEY = '758900bb596dbceb40c07f42c763b2cb'

    # GET Weather information of given city
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    data = requests.get(URL).json()
    
    # GET temparature and description from reponse
    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    # Create return result
    result = [{'temp' : temp, 'desc' : desc}]

    return result