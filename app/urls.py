from django.urls import path

from . import views


app_name = 'app'

urlpatterns = [
	path('', views.index, name='index'),
	path(r'about_us', views.about_us, name='about_us'),
	path(r'what_we_do', views.what_we_do, name='what_we_do'),
	path(r'service_pricing', views.service_pricing, name='service_pricing'),
	path(r'contact', views.contact, name='contact'), 
	path(r'contact_sent', views.contact_sent, name='contact_sent'),
	path(r'corporate', views.corporate, name='corporate'),
	path(r'school', views.school, name='school'),
	path(r'assisted_living', views.assisted_living, name='assisted_living'),
	path(r'private', views.private, name='private'),
	path(r'onsite', views.onsite, name='onsite'),
]

