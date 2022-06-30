from django.contrib import admin
from django.urls import path, include
from . import views
app_name ='trainee'
urlpatterns = [

    path('', views.the_list, name='list'),
    path('insert', views.insert, name='insert'),
    path('update/<id>', views.trainee_update, name='update'),
    path('delete<id>', views.trainee_delete, name='delete'),
    path('insertform', views.insertform, name='insertform'),
    path('updateform/<pk>', views.Updateform.as_view(), name='updateform'),
    path('classdelete/<pk>', views.ClassDelete.as_view(), name='classdelete'),

]