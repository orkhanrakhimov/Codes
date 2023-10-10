import requests
import numpy as np
import csv
from datetime import datetime
from bs4 import BeautifulSoup

# Constants
EBAY_URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=macbook+pro+m2&_sacat=0"
SEARCH_PARAMS = {
    '_from': 'R40',
    '_trksid': 'p2380057.m570.l1313',
    '_nkw': 'macbook+pro+m2',
    '_sacat': '0'
}

def get_prices_by_link(link):
    try:
        # user-agent header
        headers = {'User-Agent': 'Your User Agent'}

        # GET request with parameters
        r = requests.get(link, headers=headers)
        r.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the page
        page_parse = BeautifulSoup(r.text, 'html.parser')
        search_results = page_parse.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})

        item_prices = []

        for result in search_results:
            price_as_text = result.find("span", {"class": "s-item__price"}).text
            if "to" in price_as_text:
                continue
            price = float(price_as_text[1:].replace(",", ""))
            item_prices.append(price)
        return item_prices
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def get_average(prices):
    return np.mean(prices)

def save_to_file(prices):
    fields = [datetime.today().strftime("%B-%d-%Y"), np.around(get_average(prices), 2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

if __name__ == "__main__":
    # Build the eBay URL with search parameters
    ebay_url = f"{EBAY_URL}?{('&'.join([f'{k}={v}' for k, v in SEARCH_PARAMS.items()]))}"
    
    prices = get_prices_by_link(ebay_url)
    
    if prices:
        prices_without_outliers = remove_outliers(prices)
        average_price = get_average(prices_without_outliers)
        print("Average Price:", average_price)
        save_to_file(prices)
