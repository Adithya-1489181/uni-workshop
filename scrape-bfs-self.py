import requests
from bs4 import BeautifulSoup

res = requests.get("https://nmmsadmin.akankshatrust.in/test")
doc = BeautifulSoup(res.text, "html.parser")
print(doc.body)
