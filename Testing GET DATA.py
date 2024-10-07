#https://data.snb.ch/api/cube/snbbipo/data/csv/en

import requests
data = requests.get('https://data.snb.ch/api/cube/snbbipo/data/csv/en').text

data_text = str(data).splitlines()[-6].split(':')

#rate=float(data_text[2].replace('"',''))

print(data_text)