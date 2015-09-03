from urllib.request import urlopen
from urllib.error import URLError
from urllib.request import Request
import json
from lolbet.models import Streamer,SummonersName,Game,Player

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
		
		try:
			dictionnary = json.loads(dataInStr)
		except ValueError:
			print("probleme parsing json")
	except URLError as e: #remplacer par Urlerror?
		print(e.code)

	
	return dictionnary

#Return the summonerId of a summonersName of a region
#If the summonersName does not exist in the specified region it returns -1
def getSummonersId(summonersName,region):
	version = "v1.4"
	url = "https://{0}.api.pvp.net/api/lol/{0}/{1}/summoner/by-name/{2}?api_key={3}".format(region,version,summonersName,apiKey)
	dictionnary = urlToDict(url)
	print(dictionnary)
	print(url)
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


def streamGetDict(channelName):
	url = "https://api.twitch.tv/kraken/streams/{0}".format(channelName)
	req = Request(url,data=None,headers={'Accept': 'application/vnd.twitchtv.v3+json','Client-ID': 'ixze1gb3yw0x5vvdatj3iiklksvnk48'})
	dictionnary = urlToDict(req)
	if len(dictionnary) == 0:
		return dict()
	else:
		return dictionnary

def fillSumId(sumNameList):
	for sumName in sumNameList:
			if sumName.nameId is None:
				id = getSummonersId(sumName.name,sumName.region)
				print(sumName.name)
				print(sumName.region)	
				if id != -1:
					sumName.nameId = id
					sumName.save()

def getChampionList(region):
	version = "v1.2"
	url = "https://global.api.pvp.net/api/lol/static-data/{0}/{1}/champion?dataById=true".format(region,version)
	req = Request(url,data=None,headers={'X-Riot-Token': apiKey})
	dictionnary = urlToDict(req)
	if len(dictionnary) ==0:
		return dict()
	else:
		return dictionnary

def getSummonerSpellList(region):	
	version = "v1.2"
	url = "https://global.api.pvp.net/api/lol/static-data/{0}/{1}/summoner-spell?dataById=true".format(region,version)
	req = Request(url,data=None,headers={'X-Riot-Token': apiKey})
	dictionnary = urlToDict(req)
	if len(dictionnary) ==0:
		return dict()
	else:
		return dictionnary

def getPlayerLeagueByIds(liste,region):
	version = "v2.5"
	idString = ""
	for item in liste:
		idString = idString + "," + str(item)
	idString = idString[1:]
	print(idString)
	url = "https://na.api.pvp.net/api/lol/{0}/{1}/league/by-summoner/{2}/entry?api_key=0f161ba9-ce84-42ab-b53d-2dbe14dd2f83".format(region,version,idString)
	print(url)
	dictionnary = urlToDict(url)
	
	if len(dictionnary) == 0:
		return dict()
	
	return dictionnary



def lookUpStreamer(streamer):
	sumNameList = streamer.summonersname_set.all()
	fillSumId(sumNameList)
	for sumName in sumNameList:
		if sumName.nameId is not None:
			dictionnary = getCurrentGameDictionnary(sumName.nameId,sumName.region)
			if len(dictionnary) == 0:
				if hasattr(sumName,'game'):
					game = sumName.game
					playerList = game.player_set.all()
					for player in playerList:
						player.delete()
					game.delete()
			else:
				if hasattr(sumName,'game'):
					game = sumName.game
					playerList = game.player_set.all()
					for player in playerList:
						player.delete()
					game.delete()
				#On vérifie que l'utilisateur est en ranked
				if dictionnary['gameQueueConfigId'] == 4:
					championDictionnary = getChampionList(sumName.region)
					summonerSpellDictionnary = getSummonerSpellList(sumName.region)
					summonersIdList = list()
					for participant in dictionnary['participants']:
						summonersIdList.append(participant['summonerId'])
					leaguePlayerDictionnary = getPlayerLeagueByIds(summonersIdList,sumName.region)

		
					bannedChampions0 = (championDictionnary['data'][str(dictionnary['bannedChampions'][0]['championId'])]['name']).replace(" ","").replace("'","")
					bannedChampions1 = (championDictionnary['data'][str(dictionnary['bannedChampions'][2]['championId'])]['name']).replace(" ","").replace("'","")
					bannedChampions2 = (championDictionnary['data'][str(dictionnary['bannedChampions'][4]['championId'])]['name']).replace(" ","").replace("'","")
					bannedChampions3 = (championDictionnary['data'][str(dictionnary['bannedChampions'][1]['championId'])]['name']).replace(" ","").replace("'","")
					bannedChampions4 = (championDictionnary['data'][str(dictionnary['bannedChampions'][3]['championId'])]['name']).replace(" ","").replace("'","")
					bannedChampions5 = (championDictionnary['data'][str(dictionnary['bannedChampions'][5]['championId'])]['name']).replace(" ","").replace("'","")


					partie = Game(gameId=dictionnary['gameId'],gameStartTime = dictionnary['gameStartTime'],summonersName = sumName, bannedChampions0= bannedChampions0,bannedChampions1=bannedChampions1,bannedChampions2=bannedChampions2,bannedChampions3= bannedChampions3,bannedChampions4=bannedChampions4,bannedChampions5=bannedChampions5)
					partie.save()
	
					for participant in dictionnary['participants']:
						joueur = Player(name=participant['summonerName'], champion = (championDictionnary['data'][str(participant['championId'])]['name']).replace(" ","").replace("'",""),summonerId = participant['summonerId'],spell1 = (summonerSpellDictionnary['data'][str(participant['spell1Id'])]['name']).replace("Ignite","Dot"),spell2= (summonerSpellDictionnary['data'][str(participant['spell2Id'])]['name']).replace("Ignite","Dot"),game=partie)
						
						joueur.tier = (leaguePlayerDictionnary[str(participant['summonerId'])][0]['tier']).lower()
						joueur.leaguePoints = leaguePlayerDictionnary[str(participant['summonerId'])][0]['entries'][0]['leaguePoints']
						joueur.wins = leaguePlayerDictionnary[str(participant['summonerId'])][0]['entries'][0]['wins']
						joueur.losses = leaguePlayerDictionnary[str(participant['summonerId'])][0]['entries'][0]['losses']
						joueur.division = leaguePlayerDictionnary[str(participant['summonerId'])][0]['entries'][0]['division']
						joueur.save()
