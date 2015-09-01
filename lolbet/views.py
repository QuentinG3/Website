from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from lolbet.tasks import add
from lolbet.models import Streamer

def home(request):

	text = """	<html>
					<head>
					</head>
					<body>
						<h1> Bienvenue sur mon Website !!! </h1>
						<p> La j'ai rien a dire mais j'aurais bientôt pti téest des accèent </p>
					</body>
				</html>"""
	return HttpResponse(text)

def date(request):
	#updateCurrentGame()
	return render(request,'lolbet/date.html',{'date':datetime.now(),'streamers':Streamer.objects.all()})
	

			


