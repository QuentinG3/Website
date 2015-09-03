from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from lolbet.tasks import add
from lolbet.models import Streamer,Profil
from lolbet.forms import SignUpForm
from django.contrib.auth.models import User

def date(request):
	#updateCurrentGame()
	return render(request,'lolbet/date.html',{'date':datetime.now(),'streamers':Streamer.objects.all()})
	
def home(request):
	error = list()
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = SignUpForm(request.POST)  # Nous reprenons les données
		username = form['username']

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides

			# Ici nous pouvons traiter les données du formulaire
			email = form.cleaned_data['email']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			verifyAge = form.cleaned_data['verifyAge']

            # Créer utilisateur
			if password1==password2:
				user = User.objects.create_user(username,email,password1)
				Profil(user=user,verifyAge=verifyAge).save()
		else:
			data = list()
			print(username)
			error.append(data)

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = SignUpForm()  # Nous créons un formulaire vide
	Streamers = Streamer.objects.filter(online=True)
	# Add a comma after 3 digits
	for item in Streamers:
		item.viewers = '{0:,}'.format(item.viewers)
	return render(request,'lolbet/home.html',locals())