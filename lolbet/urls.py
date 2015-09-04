from django.conf.urls import patterns,url

urlpatterns = patterns('lolbet.views',
	url(r'^$','home'),
	url(r'^date$','date'),
	url(r'^disconnect$','deconnexion'),
	url(r'^login$','connection'),
	url(r'^register$','register'),
	url(r'^FAQ$','faq'),
	url(r'^contactus$','contact'),
	url(r'^ranking$','rank'),
	url(r'^about$','about'),
	url(r'^privacy$','privacy'),
	url(r'^streamer/(\w+)$','streamer'),
	url(r'^send$','send'),

	)