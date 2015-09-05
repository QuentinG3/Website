from django.db import models
from django.contrib.auth.models import User
import time
from django.utils import timezone




class Streamer(models.Model):
	name = models.CharField(max_length = 100)
	channelName = models.CharField(max_length = 100)
	status = models.CharField(max_length = 200,default="")
	online = models.BooleanField(default=False)
	viewers = models.IntegerField(default=0)
	preview = models.CharField(max_length = 200,default="")
	dateCreation = models.DateTimeField(auto_now_add=True)
	dateModification = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

	def timeSinceLastUpdate(self):
		return (timezone.now()-self.dateModification).total_seconds()



class SummonersName(models.Model):
	name = models.CharField(max_length = 100)
	nameId = models.BigIntegerField(null=True)
	region = models.CharField(max_length = 5)
	streamer = models.ForeignKey('Streamer')
	dateCreation = models.DateTimeField(auto_now_add=True)
	dateModification = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

	def getGameTime(self):
		nowTime = int(time.time())*1000
		return nowTime-int(self.gameStartTime)

class Game(models.Model):
	gameId = models.BigIntegerField()
	gameStartTime = models.BigIntegerField()
	summonersName = models.OneToOneField(SummonersName)
	bannedChampions0 = models.CharField(max_length = 100,null=True)
	bannedChampions1 = models.CharField(max_length = 100,null=True)
	bannedChampions2 = models.CharField(max_length = 100,null=True)
	bannedChampions3 = models.CharField(max_length = 100,null=True)
	bannedChampions4 = models.CharField(max_length = 100,null=True)
	bannedChampions5 = models.CharField(max_length = 100,null=True)

	
	def __str__(self):
		return "{0} in game number {1}".format(self.summonersName.name,self.gameId)

	def getGameTime(self):
		nowTime = int(time.time())*1000
		return nowTime-int(self.gameStartTime)

class Player(models.Model):
	champion = models.CharField(max_length = 100,null=True)
	spell1 = models.CharField(max_length = 100,null=True)
	spell2 = models.CharField(max_length = 100,null=True)
	summonerId = models.BigIntegerField()
	name = models.CharField(max_length = 100,null=True)
	tier = models.CharField(max_length = 100,null=True)
	division = models.CharField(max_length = 100,null=True)
	wins = models.BigIntegerField(null=True)
	losses = models.BigIntegerField(null=True)
	leaguePoints = models.BigIntegerField(null=True)
	game = models.ForeignKey('Game')

	def __str__(self):
		return "{0} jour le champion {1}".format(self.summonerId,self.champion)



class Profil(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length = 30, null=True)
	elo = models.IntegerField(default = 1200)
	verifyAge = models.DateField(null=True)

	def __str__(self):
		return "Profil de {0}".format(self.user.username)

class Bet(models.Model):
	user = models.ForeignKey(User)
	summonersName = models.ForeignKey('SummonersName')
	gameId = models.IntegerField()
	won = models.BooleanField()
	amount = models.IntegerField(null=True)
	dateCreation = models.DateTimeField(auto_now_add=True)
	dateModification = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "User {0} bet won:{1} on game {2}".format(self.user.username,self.won,self.gameId)