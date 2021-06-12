import os  # used to obtain environment variables from .env file
from dotenv import load_dotenv  # used to obtain environment variables from .env file
import requests  # used to make API requests
import sys  # used for sys.exit() function

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
        print("Invalid input. Please provide a properly formatted stock symbol.")
    else:
        break

# Format user input to uppercase for use with API
# Upper function found on W3Schools (https://www.w3schools.com/python/ref_string_upper.asp)
symbol_formatted = symbol.upper()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)

# Utilizes sys.exit() to exit program if there is an error fetching data from API
if "Error Message" in response.text:
    print("We're sorry, there was an error fetching data from the API. Please re-run the program to try again.")
    sys.exit()

print(type(response))
print(response.text)