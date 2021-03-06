from django.conf.urls import url
from . import views, forms

urlpatterns = [
	url(r'^test$', views.index, name='index'),
	url(r'^saveBoothDetails/$', views.BoothOwnerProfile, name='saveBoothDetails'),
	url(r'^viewBoothList/$', views.view_booth_List, name='viewBoothList'),
	url(r'^viewProductsDetails/$', views.view_products_details, name='viewProductsDetails'),
	url(r'^viewProductsList/$', views.view_Products_list, name='viewProductsList'),
	url(r'^viewBoothProducts/(?P<booth_Id>[0-9]+)/$', views.view_booth_products, name='viewBoothProducts'),
	url(r'^advertisements$', views.advertisements, name='advertisement'),
	url(r'^checkServer', views.checkServer, name='checkServer'),
	url(r'^homepage', views.homepage, name='homepage'),
]
