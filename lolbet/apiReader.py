from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import Request
import json

#API key for Riot API
apiKey = "0f161ba9-ce84-42ab-b53d-2dbe14dd2f83"
#Client key for Twitch API
clientId = "ixze1gb3yw0x5vvdatj3iiklksvnk48"

#Return a dictionnary with the informations taken from the url
#If there was a probleme trying to gather the infomations, it prints the error code and returns an empty dictonnary
def urlToDict(url):
	dictionnary = dict()
	try:
		htmlInBytes = urlopen(url)
		dataInBytes = htmlInBytes.read()
		dataInStr = dataInBytes.decode("utf-8")
		dictionnary = json.loads(dataInStr)
	except HTTPError as e: #remplacer par Urlerror?
		print(e.code)

	return dictionnary

#Return the summonerId of a summonersName of a region
#If the summonersName does not exist in the specified region it returns -1
def getSummonersId(summonersName,region):
	version = "v1.4"
	url = "https://{0}.api.pvp.net/api/lol/{0}/{1}/summoner/by-name/{2}?api_key={3}".format(region,version,summonersName,apiKey)
	dictionnary = urlToDict(url)
	print(dictionnary)
	if len(dictionnary) == 0:
		return -1
	
	return dictionnary[summonersName]['id']


#Returns a dictionnary with the informations of a summonersId of a region
#If the summoners does not exist or the player is not in a game it returns an empty dictionnary
#Note : Only work for EUW and NA right now 
def getCurrentGameDictionnary(summonersId,region):
	if region == "euw":
		region2 = "EUW1"
	elif region == "na":
		region2 = "NA1"	

	url = "https://{0}.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/{1}/{2}?api_key={3}".format(region,region2,summonersId,apiKey)
	dictionnary = urlToDict(url)
	if len(dictionnary) == 0:
		return dict()
	
	return dictionnary

#Return a dictionnary of a summonersId of a region
#If the summonersName does not exist in the specified region it returns -1
def getSummonersGameList(summonersId,region):
	version = "v1.3"
	url = "https://{0}.api.pvp.net/api/lol/{0}/{1}/game/by-summoner/{2}/recent?api_key={3}".format(region,version,summonersId,apiKey)
	dictionnary = urlToDict(url)
	if len(dictionnary) == 0:
		return dict()
	
	return dictionnary

### TO GET A WIN FROM THE SUMMONERS GAME LIST DO : data['games'][0]['stats']['win']

def tableauSummonersGameList(summonersId,region):
	dictionnary = getSummonersGameList(summonersId,region)
	liste = list()
	if len(dictionnary) == 0:
		return list()
	for i in range(0,len(dictionnary['games'])):
		liste.append((dictionnary['games'][i]['gameId'],dictionnary['games'][i]['stats']['win']))
	return liste



#Is channel does not exist return false
def streamIsOnline(channelName):
	url = "https://api.twitch.tv/kraken/streams/{0}".format(channelName)
	req = Request(url,data=None,headers={'Accept': 'application/vnd.twitchtv.v3+json','Client-ID': 'ixze1gb3yw0x5vvdatj3iiklksvnk48'})
	dictionnary = urlToDict(req)
	if len(dictionnary) == 0:
		print("ChannelName {0} n'existe pas".format(channelName))
		return False
	if dictionnary['stream'] is None:
		return False
	else:
		return True







						
				
		





			
			


