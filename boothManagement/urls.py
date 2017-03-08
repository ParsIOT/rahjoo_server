from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.save_booth_details, name='index'),
	url(r'^saveBoothDetails/$', views.save_booth_details, name='saveBoothDetails'),
	url(r'^viewBoothList/$', views.view_booth_List, name='viewBoothList'),
	url(r'^viewProductsDetails/$', views.view_products_details, name='viewProductsDetails'),
]
