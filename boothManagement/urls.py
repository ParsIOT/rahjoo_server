from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.save_booth_details, name='index'),
	url(r'^saveBoothDetails/$', views.save_booth_details, name='saveBoothDetails'),
	url(r'^viewBoothDetails/$', views.view_booth_details, name='viewBoothDetails')
]
