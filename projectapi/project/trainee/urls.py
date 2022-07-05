from django.urls import path
from .views import *

app_name = 'trainee'
urlpatterns = [
    path('insert/',insert,name='insert'),
    path('list',List,name='alllist'),
    path('list/<id>',GETCOURSE,name='listid'),
    path('update/',update),
    path('delete/<id>',delete),
]