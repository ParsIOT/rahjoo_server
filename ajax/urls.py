from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^editProductDetails/$', views.editProductDetails, name='editProductDetails'),
	url(r'^newProductDetails/$', views.newProductDetails, name='newProductDetails'),
	url(r'^makeAdvertisementsOrder/$', views.makeAdvertisementsOrder, name='makeAdvertisementsOrder'),
    url(r'^getAdvertisementAreas/$', views.getAdvertisementAreas, name='getAdvertisementAreas'),

]
