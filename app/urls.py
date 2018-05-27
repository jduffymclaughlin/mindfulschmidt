from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
	path('', views.index, name='index'),
	path('about_us', views.about_us, name='about_us'),
	path('what_we_do', views.what_we_do, name='what_we_do'),
	path('service_pricing', views.service_pricing, name='service_pricing'),
	path(r'contact', views.contact, name='contact'), 
	path(r'contact_sent', views.contact_sent, name='contact_sent'),
]

