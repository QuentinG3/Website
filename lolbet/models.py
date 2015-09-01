from django.db import models
from django.contrib.auth.models import User
import time

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

	def __str__(self):
		return "{0} in game number {1}".format(self.summonersName.name,self.gameId)

	def getGameTime(self):
		nowTime = int(time.time())*1000
		return nowTime-int(self.gameStartTime)

class Player(models.Model):
	championId = models.BigIntegerField()
	spell1Id = models.BigIntegerField()
	spell2Id = models.BigIntegerField()
	summonerId = models.BigIntegerField()
	teamId = models.BigIntegerField()
	profilIcanId = models.BigIntegerField()
	game = models.ForeignKey('Game')

	def __str__(self):
		return "{0} jour le champion {1}".format(self.summonerId,self.championId)



class Profil(models.Model):
	user = models.OneToOneField(User)
	elo = models.IntegerField(default = 1200)

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





