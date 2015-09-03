from django.conf.urls import patterns,url

urlpatterns = patterns('lolbet.views',
	url(r'^$','home'),
	url(r'^date$','date'),
	url(r'^deconnexion$','deconnexion'),
	url(r'^streamer/(\w+)$','streamer'),
	)