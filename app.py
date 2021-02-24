from flask import Flask, render_template
import weather 
import stock
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # GET Porvoo Weather Information
    porvoo_result = weather.get_weather_info('porvoo')
    # GET Seoul Weather
    seoul_result = weather.get_weather_info('seoul')

    # Get Stock Information   
    samsung_result = stock.get_stock_info('https://finance.yahoo.com/quote/005930.KS?p=005930.KS&.tsrc=fin-srch')
    kakao_result = stock.get_stock_info('https://finance.yahoo.com/quote/035720.KS?p=035720.KS&.tsrc=fin-srch')
    apple_result = stock.get_stock_info('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch')
    tesla_result = stock.get_stock_info('https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch')
    neste_result = stock.get_stock_info('https://finance.yahoo.com/quote/NESTE.HE?p=NESTE.HE&.tsrc=fin-srch')
    stocks=[{'samsung' : samsung_result, 'kakao' : kakao_result, 'apple' : apple_result, 'tesla' : tesla_result, 'neste' : neste_result}]


    return render_template('main.html', 
                            porvoo = porvoo_result,  
                            seoul = seoul_result,
                            stocks = stocks
                            )

if __name__ == '__main__':
    app.run()