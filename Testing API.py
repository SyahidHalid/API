#Link : https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/

#pip install requests

#import requests

#test 1

import requests
import json
# Function to get live stock data for a symbol
def get_stock_data():
    url = f&quot;https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&amp;symbol=IBM&amp;interval=5min&amp;outputsize=full&amp;apikey=demo&quot;
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data[&quot;Meta Data&quot;][&quot;3. Last Refreshed&quot;]
        price = data[&quot;Time Series (5min)&quot;][last_refreshed][&quot;1. open&quot;]
        return price
    else:
        return None

stock_prices = {}
price = get_stock_data()
symbol=&quot;IBM&quot;
if price is not None:
    stock_prices[symbol] = price

print(f&quot;{symbol}: {price}&quot;)

#Codes related to “GET” request:
#200 OK: The server successfully processed the request, and the requested data is returned.
#201 Created: A new resource is created on the server as a result of the request.
#204 No Content: The request is successful, but there is no additional data to return.
#300 Multiple Choices: The requested resource has multiple representations, each with its own URL.
#302 Found (Temporary Redirect): The requested resource is temporarily located at a different URL.
#304 Not Modified: The client’s cached copy of the resource is still valid, and no re-download is necessary.
#400 Bad Request: The request has malformed syntax or contains invalid data, making it incomprehensible to the server.
#401 Unauthorized: Authentication is required, and the client’s credentials (e.g., API key) are missing or invalid.
#500 Internal Server Error: An unexpected server error occurred during request processing.
#502 Bad Gateway: Acting as a gateway or proxy, the server received an invalid response from an upstream server.

#test 2

import requests
# Replace 'API_KEY' with your actual API key from NewsAPI
API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
url = f&quot;https://newsapi.org/v2/top-headlines?country=us&amp;category=business&amp;apiKey={API_KEY}&quot;
response = requests.get(url)
print(response.status_code)

#test 3

import json
import requests

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        for index, article in enumerate(articles[:3], start=1):
            print(f&quot;Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n&quot;)
    else:
        print(f&quot;Error: {response.status_code}&quot;)

API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
api_endpoint = f&quot;https://newsapi.org/v2/top-headlines?country=us&amp;category=business&amp;apiKey={API_KEY}&quot;

fetch_and_print_articles(api_endpoint)

def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))

# Example usage:
# jprint(response.json())

#test 4

import requests

# API endpoint and key
API_URL = &quot;https://newsapi.org/v2/top-headlines&quot;
API_KEY = &quot;3805f6bbabcb42b3a0c08a489baf603d&quot;

# Parameters for the API request
params = {
    &quot;country&quot;: &quot;us&quot;,
    &quot;apiKey&quot;: API_KEY
}

# Making the API request
response = requests.get(API_URL, params=params)

# Checking if the request was successful
if response.status_code == 200:
    # Printing the JSON response
    print(response.json())
else:
    print(f&quot;Error: {response.status_code}&quot;)

#test 5

# Python's built-in support for JSON
import json 
# Python turtle library for creating designs and images
import turtle  
# Python module for fetching URLs
import urllib.request  
# Python module for time-related functions
import time  
# Python module for opening URLs in a web browser
import webbrowser  
# Python module for retrieving latitude and longitude
import geocoder  

url = "http://api.open-notify.org/astros.json" 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==

Sure, I can help you create a simple API for your Python script using Flask, a lightweight web framework. Here’s a basic example to get you started:
    
#pip install Flask

#2. Create Your Python Script: Let’s assume you have a Python script named script.py with a function you want to expose via an API:

# script.py
def my_function(param):
    return f"Hello, {param}!"

#3. Create the Flask API: Now, create a new file named app.py and set up your Flask API

from flask import Flask, request, jsonify
from script import my_function

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    param = request.args.get('param')
    result = my_function(param)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


#4. Run Your API: Run your Flask app by executing the following command in your terminal:

python app.py


#5. Test Your API: You can test your API by opening a web browser or using a tool like Postman and navigating to:

http://127.0.0.1:5000/api?param=World

#This should return a JSON response:

{
    "result": "Hello, World!"
}

This is a basic example to get you started. You can expand this by adding more routes, handling different HTTP methods (POST, PUT, DELETE), and adding error handling as needed. If you have any specific requirements or need further customization, feel free to ask!
