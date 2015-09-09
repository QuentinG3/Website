from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from lolbet.tasks import add
from lolbet.models import Streamer,Profil, SummonersName, Game, Player
from lolbet.forms import SignUpForm
from lolbet.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from lolbet.apiReader import lookUpStreamer
import json
from django.db.models.fields.related import ManyToManyField
from django.core import serializers


def send(request):
	data = list()
	data.append(1)
	data.append(2)
	data.append(3)
	jso = dict()
	jso['lol'] = data
	print(jso)
	return HttpResponse(json.dumps(jso))


def username_present(username):
	if User.objects.filter(username=username).exists():
		return True

	return False

def email_present(email):
    if User.objects.filter(email =email).exists():
        return True

    return False

def gameInfo(request):

	channelName = request.POST['channelName']
	streamer=Streamer.objects.filter(channelName=channelName)[0]
	#lookUpStreamer(streamer)


	summonerName=SummonersName.objects.filter(streamer=streamer)
	inGameSummoner = list()
	for item in summonerName:
		if hasattr(item, 'game'):
			inGameSummoner.append(item)
	if len(inGameSummoner) == 0:
		print("return false")
		return HttpResponse(False)
	

	game=inGameSummoner[0].game
	players=Player.objects.filter(game=game)

	team1=list(players[0:5])
	team2=list(players[5:10])

	jsonData = dict()
	jsonData['summonerName'] = inGameSummoner[0].name
	jsonData['gameId'] = game.gameId
	jsonData['region'] = inGameSummoner[0].region
	jsonData['team1'] = list()
	jsonData['team2'] = list()
	for item in team1:
		player = dict()
		player['name'] = item.name
		player['champion'] = item.champion
		player['wins'] = item.wins
		player['losses'] = item.losses
		player['division'] = item.division
		player['tier'] = item.tier
		player['leaguePoints'] = item.leaguePoints
		player['spell1'] = item.spell1
		player['spell2'] = item.spell2
		jsonData['team1'].append(player)

	for item in team2:
		player = dict()
		player['name'] = item.name
		player['champion'] = item.champion
		player['wins'] = item.wins
		player['losses'] = item.losses
		player['division'] = item.division
		player['tier'] = item.tier
		player['leaguePoints'] = item.leaguePoints
		player['spell1'] = item.spell1
		player['spell2'] = item.spell2
		jsonData['team2'].append(player)

	jsonData['banned1']=list()
	jsonData['banned2']=list()
	jsonData['banned1'].append(game.bannedChampions0)
	jsonData['banned1'].append(game.bannedChampions1)
	jsonData['banned1'].append(game.bannedChampions2)

	jsonData['banned2'].append(game.bannedChampions3)
	jsonData['banned2'].append(game.bannedChampions4)
	jsonData['banned2'].append(game.bannedChampions5)

	return HttpResponse(json.dumps(jsonData))


def streamer(request,channelName):
	return render(request,'lolbet/overview.html',locals())

def date(request):
	#updateCurrentGame()
	return render(request,'lolbet/date.html',{'date':datetime.now(),'streamers':Streamer.objects.all()})

def faq(request):
	return render(request,'lolbet/faq.html',locals())

def contact(request):
	return render(request,'lolbet/contact.html',locals())

def rank(request):
	return render(request,'lolbet/rank.html',locals())

def about(request):
	return render(request,'lolbet/about.html',locals())

def privacy(request):
	return render(request,'lolbet/privacy.html',locals())

def register(request):
	jso = dict()
	jso['username'] = "ok"
	jso['email'] = "ok"

	valid=True

	signUpForm = SignUpForm(request.POST)  # Nous reprenons les données

	if signUpForm.is_valid(): # Nous vérifions que les données envoyées sont valides

			# Ici nous pouvons traiter les données du formulaire
		username = signUpForm.cleaned_data['username'].lower()
		email = signUpForm.cleaned_data['email'].lower()
		password1 = signUpForm.cleaned_data['password1']
		password2 = signUpForm.cleaned_data['password2']
		verifyAge = signUpForm.cleaned_data['verifyAge']

			#Check username already in DB
		if(username_present(username)):
			valid = False
			jso['username'] = "not"

			#check email already in DB
		if(email_present(email)):
			valid = False
			jso['email'] = "not"

			#Create User 
		if(valid):
			user = User.objects.create_user(username,email,password1)
			Profil(user=user,username=signUpForm.cleaned_data['username'],verifyAge=verifyAge).save()

			login(request, authenticate(username=username, password=password1))

	return HttpResponse(json.dumps(jso))

def connect(request):
	valid=False
	loginForm = LoginForm(request.POST)
	if loginForm.is_valid():
		username = loginForm.cleaned_data["username"].lower()
		password = loginForm.cleaned_data["password"]
		
		user = authenticate(username=username, password=password)

		if user:
			valid=True
			login(request, user)

	return HttpResponse(valid)

def deconnexion(request):
    logout(request)
    return redirect(reverse(home))
	
def home(request):
	Streamers = Streamer.objects.filter(online=True)
	# Add a comma after 3 digits
	for item in Streamers:
		item.viewers = '{0:,}'.format(item.viewers)
	return render(request,'lolbet/home.html',locals())