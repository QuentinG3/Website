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

def username_present(username):
	if User.objects.filter(username=username).exists():
		return True

	return False

def email_present(email):
    if User.objects.filter(email =email).exists():
        return True

    return False


def streamer(request,name):
	errorUser = False
	errorEmail = False
	errorLogin = False
	errorData = list()

	valid = True

	if request.method == 'POST':  # S'il s'agit d'une requête POST
		signUpForm = SignUpForm(request.POST)  # Nous reprenons les données
		loginForm = LoginForm(request.POST) #on reprends les données
		
		if loginForm.is_valid(): # On a affaire à une connection
			username = loginForm.cleaned_data["username"]
			password = loginForm.cleaned_data["password"]

			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
			else:
				errorData.append(username)
				errorLogin = True

		if signUpForm.is_valid(): # Nous vérifions que les données envoyées sont valides

			# Ici nous pouvons traiter les données du formulaire
			username = signUpForm.cleaned_data['username'].lower()
			email = signUpForm.cleaned_data['email'].lower()
			password1 = signUpForm.cleaned_data['password1']
			password2 = signUpForm.cleaned_data['password2']
			verifyAge = signUpForm.cleaned_data['verifyAge']

			#Check username already in DB
			if(username_present(username)):
				errorUser=True
				valid = False

			#check email already in DB
			if(email_present(email)):
				errorEmail=True
				valid = False

			#Create User 
			if(valid):
				user = User.objects.create_user(username,email,password1)
				Profil(user=user,verifyAge=verifyAge).save()
			else:
				errorData.append(username)
				errorData.append(email)
				errorData.append(password1)
				errorData.append(password2)
				errorData.append(verifyAge)

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		signUpForm = SignUpForm()  # Nous créons un formulaire vide
		loginForm = LoginForm(request.POST)
	'''
	streamer=Streamer.objects.filter(name=name)[0]
	lookUpStreamer(streamer)
	summonerName=SummonersName.objects.filter(streamer=streamer)
	gameList = list()
	for item in summonerName:
		if hasattr(item, 'game'):
			gameList.append(item)


	game=Game.objects.filter(summonersName=gameList[0])[0]
	players=Player.objects.filter(game=game)

	team1=players[0:5]
	team2=players[5:10]
	'''

	return render(request,'lolbet/overview.html',locals())

def date(request):
	#updateCurrentGame()
	return render(request,'lolbet/date.html',{'date':datetime.now(),'streamers':Streamer.objects.all()})

def deconnexion(request):
    logout(request)
    return redirect(reverse(home))
	
def home(request):
	errorUser = False
	errorEmail = False
	errorLogin = False
	errorData = list()

	valid = True

	if request.method == 'POST':  # S'il s'agit d'une requête POST
		signUpForm = SignUpForm(request.POST)  # Nous reprenons les données
		loginForm = LoginForm(request.POST) #on reprends les données
		
		if loginForm.is_valid(): # On a affaire à une connection
			username = loginForm.cleaned_data["username"]
			password = loginForm.cleaned_data["password"]

			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
			else:
				errorData.append(username)
				errorLogin = True

		if signUpForm.is_valid(): # Nous vérifions que les données envoyées sont valides

			# Ici nous pouvons traiter les données du formulaire
			username = signUpForm.cleaned_data['username'].lower()
			email = signUpForm.cleaned_data['email'].lower()
			password1 = signUpForm.cleaned_data['password1']
			password2 = signUpForm.cleaned_data['password2']
			verifyAge = signUpForm.cleaned_data['verifyAge']

			#Check username already in DB
			if(username_present(username)):
				errorUser=True
				valid = False

			#check email already in DB
			if(email_present(email)):
				errorEmail=True
				valid = False

			#Create User 
			if(valid):
				user = User.objects.create_user(username,email,password1)
				Profil(user=user,verifyAge=verifyAge).save()
			else:
				errorData.append(username)
				errorData.append(email)
				errorData.append(password1)
				errorData.append(password2)
				errorData.append(verifyAge)

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		signUpForm = SignUpForm()  # Nous créons un formulaire vide
		loginForm = LoginForm(request.POST)

	Streamers = Streamer.objects.filter(online=True)
	# Add a comma after 3 digits
	for item in Streamers:
		item.viewers = '{0:,}'.format(item.viewers)
	return render(request,'lolbet/home.html',locals())