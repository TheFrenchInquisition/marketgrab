import urllib.request, json

def fetchMeSomeData(appid, item, currency="1", debug=False):
	data = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?country=US&currency="+currency+"&appid="+appid+"&market_hash_name="+item).read()
	data = str(data)
	data = data[2:-1]
	data = json.loads(data)
	if data["success"]:
		if debug:
			print(data)
		else:
			lowest = data["lowest_price"][data["lowest_price"].index(";")+1:]
			print("Lowest price: $"+lowest)
			print("Amount for sale: "+data["volume"])

currency = "1" #1 = USD, 2 = GBP, 3 = EURO, 5 = RUB
item = "StatTrak%E2%84%A2%20P250%20%7C%20Steel%20Disruption%20%28Factory%20New%29"
game = "730" #csgo

fetchMeSomeData(game, item)
