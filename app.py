from flask import Flask, render_template
import requests
import weather 

app = Flask(__name__)

@app.route('/')
def index():
    # GET Porvoo Weather   
    porvoo_result = weather.get_weather_info('porvoo')
    # GET Seoul Weather
    seoul_result = weather.get_weather_info('seoul')
    
    return render_template('main.html', 
                            porvoo = porvoo_result,  
                            seoul = seoul_result)

if __name__ == '__main__':
    app.run()