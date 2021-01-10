from django.urls import path
from . import views

#urlpatterns = [
	#path('', views.home)
	#path('about-us', views.form,)    
#]

urlpatterns = [
	path('', views.home, name = 'index'),
	path('about', views.about, name = 'about'),
	path('contact', views.contact, name = 'contact'),
	path('buy', views.buy, name = 'buy'),
]