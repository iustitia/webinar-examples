import requests
import json

# http://api.nbp.pl/#kursyWalut

currency = "USD"

url_scheme = 'http://api.nbp.pl/api/exchangerates/rates/A/{code}/?format=json'
url = url_scheme.format(code=currency)

##############

"""Chcemy pobrać aktualny kurs waluty dolara z danych NBP za pomocą API (http://api.nbp.pl/#kursyWalut)
Odpytaj o walutę, odbierz odpowiedź, a potem wyłuskaj z nich potrzebną wartość.
"""
##############

