from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^editProductDetails/$', views.editProductDetails, name='editProductDetails'),
	url(r'^makeAdvertisementsOrder/$', views.makeAdvertisementsOrder, name='makeAdvertisementsOrder'),
    url(r'^getAdvertisementsAreas/$', views.getAdvertisementsAreas, name='getAdvertisementsAreas'),

]
