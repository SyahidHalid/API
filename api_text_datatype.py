#https://data.snb.ch/api/cube/snbbipo/data/csv/en

import requests
import pandas as pd 

data = requests.get('https://data.snb.ch/api/cube/snbbipo/data/csv/en', verify=False).text

data_text = str(data).splitlines()[-6].split(':')

#rate=float(data_text[2].replace('"',''))

print(data_text)

#load public key if path public n private key
