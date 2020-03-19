import requests
import json

# http://api.nbp.pl/#kursyWalut

currency = "USD"

url_scheme = 'http://api.nbp.pl/api/exchangerates/rates/A/{code}/?format=json'
url = url_scheme.format(code=currency)

##############

response = requests.get(url)

# 1. propozycja
parsed = response.json()
print(parsed['rates'][0]['mid'])

# 2. propozycja - bezpieczniejsza, jeśli content-type nieokreślony
data = json.loads(response.content.decode('utf-8'))
print(data['rates'][0]['mid'])
