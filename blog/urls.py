from django.urls import path, re_path

from . import views

app_name = "blog"

urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'view/(?P<slug>[^\.]+)',
    views.view_post, name='view_post')
]
