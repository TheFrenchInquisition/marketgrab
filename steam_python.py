import urllib.request

api_key = "" #http://steamcommunity.com/dev/apikey
api_url = "http://api.steampowered.com/"
method = "" #the thing we query, get it from https://wiki.teamfortress.com/wiki/WebAPI#General_interfaces

def fetchMeSomeData(itemid):
	data = urllib.request.urlopen(api_url + "" + "?key=" + api_key).read()
	print(data)
