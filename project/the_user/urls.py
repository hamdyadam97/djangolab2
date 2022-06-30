from django.urls import path, include
from . import views
app_name ='the_user'
urlpatterns = [
    path('register',views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('registerform', views.registerform, name='registerform'),

]