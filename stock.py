from bs4 import BeautifulSoup
import requests

def get_stock_info(search_url):

    req = requests.get(search_url)
    soup = BeautifulSoup(req.text, 'html.parser')

    # Get Stock Information
    now = soup.find('span', attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text.replace('.00', '')
    return now
    
