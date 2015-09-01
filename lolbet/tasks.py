from __future__ import absolute_import

#from celery import shared_task
from lolbet.models import Streamer,SummonersName,Profil,Bet,Player,Game
from lolbet.apiReader import streamIsOnline,getCurrentGameDictionnary,getSummonersId,tableauSummonersGameList,streamGetDict

#@shared_task
def add(x, y):
	return x + y



#@shared_task
def updateOnlineStream():
	allStreamer = Streamer.objects.all()
	for streamer in allStreamer:
		dictionnary = streamGetDict(streamer.channelName)
		if len(dictionnary) !=0:
			#print("{0} dict not null".format(streamer.name))
			if dictionnary['stream'] is None:
				#print("{0} stream is none".format(streamer.name))
				streamer.online = False
				streamer.status = ""
				streamer.viewers = 0
				streamer.preview = 0
				streamer.save()
			else:
				#print("{0} stream is not none".format(streamer.name))
				if dictionnary['stream']['game'] == "League of Legends":
					#print("{0} Play League of legends".format(streamer.name))
					streamer.online = True
					streamer.status = dictionnary['stream']['channel']['status']
					streamer.viewers = dictionnary['stream']['viewers']
					streamer.preview = dictionnary['stream']['preview']['medium']
					streamer.save()
	
#RAJOUTER UPDATE SEULEMENT POUR LES RANKED GAME ETC
#@shared_task
def updateCurrentGame():
	print("je suis ici")
	#allStreamers = Streamer.objects.filter(online=True)
	allStreamers = Streamer.objects.all()
	for stream in allStreamers:
		print(stream)
		summonersNameList = stream.summonersname_set.all()
		print(summonersNameList)
		for name in summonersNameList:
			if name.nameId is None:
				id = getSummonersId(name.name,name.region)
				if id != -1:
					name.nameId = id
					name.save()

			if name.nameId != None:
				dictionnary = getCurrentGameDictionnary(name.nameId,name.region)
				#Si on a une game on met a jour avec le timespamp et la game id
				#sinon on remet les champs None
				print(dictionnary)
				if len(dictionnary) == 0:
					if name.summonersName is not None:
						nameToDel = name.summonersName
						nameToDel.delete()
				else:
					if name.summonersName is None:
						partie = Game(gameId=dictionnary['gameId'],gameStartTime = dictionnary['gameStartTime'],summonersName = name).save()
					else:
						sumName = name.summonersName
						sumName.gameId = dictionnary['gameId']
						sumName.gameStartTime = dictionnary['gameStartTime']				
						sumName.save()


#@shared_task
def processBet():
	dinstinctBet = Bet.objects.values("summonersName").distinct()
	retreivedBet = dict()
	print("dinstinctBet {0}".format(dinstinctBet))
	for dinstinctBetUnit in dinstinctBet:
		sumName = SummonersName.objects.filter(id=dinstinctBetUnit['summonersName'])[0]
		string = "{0}".format(sumName.nameId)
		retreivedBet[string] = tableauSummonersGameList(sumName.nameId,sumName.region)
		
	print("retreivedBet {0}".format(retreivedBet))	
	allBets = Bet.objects.all()
	for bet in allBets:
		print(bet.summonersName.name)
		print(bet.summonersName.nameId in retreivedBet)
		for retreivedBetUnit in retreivedBet["{0}".format(bet.summonersName.nameId)]:
				if retreivedBetUnit[0] == bet.gameId:
					if retreivedBetUnit[1] == bet.won:
						profilUser = bet.user.profil
						profilUser.elo = profilUser.elo + bet.amount
						profilUser.save()
						bet.delete()
					else:
						profilUser = bet.user.profil
						profilUser.elo = profilUser.elo - bet.amount
						profilUser.save()
						bet.delete()