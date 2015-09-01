from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from lolbet.tasks import add
from lolbet.models import Streamer

def date(request):
	#updateCurrentGame()
	return render(request,'lolbet/date.html',{'date':datetime.now(),'streamers':Streamer.objects.all()})
	
def home(request):
	Streamers = Streamer.objects.filter(online=True)
	for item in Streamers:
		item.viewers = '{0:,}'.format(item.viewers)
	return render(request,'lolbet/home.html',{'streamers':Streamers})

			


