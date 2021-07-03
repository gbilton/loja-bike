import requests


data = {
  "marca": "Speciallized",
  "modelo": "Rockhopper",
  "ano": 2018,
  "cor": "Vermelha",
  "preco": 3700.00
}

url = 'http://127.0.0.1:8000/'
requests.post(url, json=data)
