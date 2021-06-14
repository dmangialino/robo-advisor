import os  # used to obtain environment variables from .env file
from dotenv import load_dotenv  # used to obtain environment variables from .env file
import requests  # used to make API requests
import sys  # used for sys.exit() function
import json  # to create list
from datetime import datetime  # to capture date and time of program execution
from pandas import DataFrame  # to use DataFrames

load_dotenv() 

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
symbol = ""

# Program utilizes to_usd function provided by Professor Rossetti to convert values to USD format
def to_usd(my_price):
    return f"${my_price:,.2f}"

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

# Capture date and time of the request / program execution
# Code for date and time adopted form thispointer.com and Stack Overflow for AM/PM (links below)
# https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/
# https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime
timestamp = datetime.now()
timestampStr = timestamp.strftime("%b-%d-%Y %I:%M %p")


# Format user input to uppercase for use with API
# Upper function found on W3Schools (https://www.w3schools.com/python/ref_string_upper.asp)
symbol_formatted = symbol.upper()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)

# Utilizes sys.exit() to exit program if there is an error fetching data from API
if "Error Message" in response.text:
    print("We're sorry, there was an error fetching data from the API. Please re-run the program to try again.")
    sys.exit()


########## WRITE HISTORICAL DATA TO CSV ##########

# Convert response from API to a dictionary
parsed_response = json.loads(response.text)

# Convert dictionary to DataFrame
response_df = DataFrame(parsed_response)

# Create formatted DataFrame to write to CSV

# Write historical data to local CSV file
### TO DO: FIX FORMATTING?????
csv_file_path = "data/prices.csv"
response_df.to_csv(csv_file_path)


########## CALCULATE REQUIRED FIELDS ##########

# Create list of dates
timeseries = parsed_response["Time Series (Daily)"]

# Calculate latest closing price (clos price on latest available day of data)
# Utilized W3Schools documentation for sort function / reverse parameter (https://www.w3schools.com/python/ref_list_sort.asp)
dates = list(timeseries.keys())
dates.sort(reverse = True)
latest_date = dates[0]
latest_close = to_usd(float(timeseries[latest_date]["4. close"]))

# Caluculate recent high price (max of high prices over past 100 days of trading data)
# Calculate recent low price (min of low prices over past 100 days of trading data)
high_prices = []
low_prices = []
for date in dates:
    high_prices.append(timeseries[date]["2. high"])
    low_prices.append(timeseries[date]["3. low"])

high_price = to_usd(float(max(high_prices)))
low_price = to_usd(float(min(low_prices)))

# Print stock information and recommendation for user
print("----------------------------------------")
print("REQUESTED STOCK MARKET DATA...")
print("REQUESTED AT:", timestampStr)
print("----------------------------------------")
print("STOCK SYMBOL:", symbol_formatted)
print("----------------------------------------")
print("LAST REFRESH:", response_df["Meta Data"]["3. Last Refreshed"])
print("LATEST CLOSING PRICE:", latest_close)
print("RECENT HIGH PRICE:", high_price)
print("RECENT LOW PRICE:", low_price)
print("----------------------------------------")
print("RECOMMENDATION:")
print("CONFIDENCE:")
print("RECOMMENDATION EXPLANATION:")
print("----------------------------------------")
