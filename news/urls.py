from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^news/', views.newsletter, name='news'),
]