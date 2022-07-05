from django.urls import path
from .views import  *
urlpatterns = [
  path('listapi',listapi,name='listapi')
]