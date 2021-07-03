import requests
import popular
import json


def post(url, table):
    for i in table.iloc:
        data = json.loads(i.to_json())
        requests.post(url, json=data)

post('http://127.0.0.1:8000/addbike', popular.produtos)
post('http://127.0.0.1:8000/addcostumer', popular.clientes)
post('http://127.0.0.1:8000/checkout', popular.vendas)
