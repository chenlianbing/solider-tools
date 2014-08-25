from django.conf.urls import patterns, url

from wages import views

urlpatterns = patterns('',
	# ex: /wages
	url(r'^$', views.calculator, name='calculator'),
	
	# ex: /wages/images/
	url(r'^images/(?P<image_name>\S+)$', views.image_show, name='image_show'),
)	