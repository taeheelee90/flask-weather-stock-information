import yfinance as yf
from datetime import datetime

def get_stock_info(company):
    today = datetime.today().strftime('%Y-%m-%d')
    return yf.download(company, start = today)
    
