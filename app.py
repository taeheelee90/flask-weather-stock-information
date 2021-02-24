from flask import Flask, render_template
import requests
import weather 
import stock


app = Flask(__name__)

@app.route('/')
def index():
    # GET Porvoo Weather   
    porvoo_result = weather.get_weather_info('porvoo')
    # GET Seoul Weather
    seoul_result = weather.get_weather_info('seoul')

    # Stock information
    company_code = {'samsung':'005930.KS', 'kakao':'035720.KS'}    
    samsung = stock.get_stock_info(company_code['samsung'])
    kakao = stock.get_stock_info(company_code['kakao'])

    return render_template('main.html', 
                            porvoo = porvoo_result,  
                            seoul = seoul_result, 
                            samsung = samsung.to_html(),
                            kakao = kakao.to_html())

if __name__ == '__main__':
    app.run()