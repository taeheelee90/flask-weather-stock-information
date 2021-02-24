from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # SET VARIABLE
    API_KEY = '758900bb596dbceb40c07f42c763b2cb'

    # GET Porvoo Weather
    PORVOO_URL = f'http://api.openweathermap.org/data/2.5/weather?q=porvoo&appid={API_KEY}&units=metric'
    porvoo_data = requests.get(PORVOO_URL).json()
    porvoo_temp = porvoo_data['main']['temp']
    porvoo_desc = porvoo_data['weather'][0]['description']
    porvoo_result = [{'temp' : porvoo_temp, 'desc' : porvoo_desc}]

    # GET Seoul Weather
    SEOUL_URL = f'http://api.openweathermap.org/data/2.5/weather?q=seoul&appid={API_KEY}&units=metric'
    seoul_data = requests.get(SEOUL_URL).json()
    seoul_temp = seoul_data['main']['temp']
    seoul_desc = seoul_data['weather'][0]['description']
    seoul_result =[{'temp' : seoul_temp, 'desc' : seoul_desc}]
    
    return render_template('main.html', porvoo = porvoo_result,  seoul = seoul_result)

if __name__ == '__main__':
    app.run()