import os
from dotenv import load_dotenv
import requests

load_dotenv() 

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
symbol = input("Please provide a stock or cryptocurrency symbol: ")

# Validate user input (between 1 and 5 characters, no numbers)


request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)

print(type(response))
print(response.text)