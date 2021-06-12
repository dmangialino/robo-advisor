import os
from dotenv import load_dotenv
import requests

load_dotenv() 

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
symbol = ""

while(True):
    symbol = input("Please provide a stock or cryptocurrency symbol: ")
    contains_digit = False
    for character in symbol:
        if character.isdigit():
            contains_digit = True

    # Validate user input (between 1 and 5 characters, no numbers)
    if (len(symbol) > 5) or (len(symbol) < 1 or symbol.isdigit() or contains_digit == True):
        print("INVALID INPUT")
    else:
        break

print("VALID SYMBOL")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)

print(type(response))
#print(response.text)