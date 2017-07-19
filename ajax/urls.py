from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^editProductDetails/$', views.editProductDetails, name='editProductDetails'),
	url(r'^newProductDetails/$', views.newProductDetails, name='newProductDetails'),
	url(r'^makeAdvertisementsOrder/$', views.makeAdvertisementsOrder, name='makeAdvertisementsOrder'),
    url(r'^getAdvertisementAreas/$', views.getAdvertisementAreas, name='getAdvertisementAreas'),
	url(r'^uploadImage/product$', views.uploadProductImage, name='uploadProductImage'),
	url(r'^uploadImage/booth$', views.uploadBoothImage, name='uploadBoothImage'),
	url(r'^uploadImage/advertisement', views.uploadAdvertisementImage, name='uploadAdvertisementImage'),
	url(r'^advertisementJson', views.advertisementJson, name='advertisementJson'),

]
