# robo-advisor

## Installation

Clone this repository to your local machine. Then, using the command line, navigate to the root folder of the repository.

## Setup

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env"

```sh
conda activate -n stocks-env python=3.8
conda activate stocks-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

## Create .env file

After activating the environment and installing the required packages, create a ".env" file to specify environment variable values to be used by the program. To do so, navigate to the root directory of the local repository and create a new file called ".env".

### Obtain Aplha Vantage API Key

This program utilizes the Alpha Vantage API to obtain stock information. To use the program, you must obtain an API key and save it in the newly created .env file. To do so, navigate to Alpha Vantage's website: https://www.alphavantage.co/support/#api-key

Then, complete the form and CAPTCHA and click "GET FREE API KEY."

Copy the API key provided and assign it to the `ALPHAVANTAGE_API_KEY` in the .env file. Be sure to put double quotes around the API key, as shown below:

`ALPHAVANTAGE_API_KEY` = "API_KEY_HERE"

## Run the App

From the virtual environment, run the Python script from the command line:

```sh
python app/robo_advisor.py
```