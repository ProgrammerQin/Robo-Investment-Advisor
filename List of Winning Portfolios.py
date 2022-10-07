import requests

# https://www.alphavantage.co/
url = 'https://www.alphavantage.co/query?function=TOURNAMENT_PORTFOLIO&season=2021-09&apikey=AEGJDU540F597MXQ'
r = requests.get(url)
data = r.json()

print(data)