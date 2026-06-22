# from flask import Flask, request, jsonify
# from API_script import my_function

# app = Flask(__name__)

# @app.route('/api', methods=['GET'])
# def api():
#     param = request.args.get('param')
#     result = my_function(param)
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)


# #http://127.0.0.1:5000/api?param=World

# # def my_function(param):
# #     return f"Hello, {param}!"

#=====================================================================================
# with parameter
#=====================================================================================

import requests
import pandas as pd

currency = "USD"
year = "2024"
month = "06"

url = f"https://api.bnm.gov.my/public/exchange-rate/{currency}/year/{year}/month/{month}"

headers = {
    "Accept": "application/vnd.BNM.API.v1+json"
}

params = {
    "session": "1700",   # optional (close rate)
    "quote": "rm"        # MYR base
}

response = requests.get(url, headers=headers, params=params, verify=False)

data = response.json()

# convert to DataFrame
df = pd.json_normalize(data['data']['rate'])

print(df.head())
