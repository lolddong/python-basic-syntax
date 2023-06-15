import requests
from bs4 import BeautifulSoup
import time
import json
url = "https://api.binance.com/api/v3/ticker/24hr"
import seaborn
from matplotlib import pyplot
import pandas
file_path = '/Users/dayoonz/Desktop/안다윤/tips.csv'  
csv_data = pandas.read_csv(file_path)
print(csv_data)
