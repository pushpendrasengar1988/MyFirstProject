from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.getLogin, name='getLogin'),
    path('signin', views.postLogin, name='postLogin'),
    path('register', views.getRegister, name='getRegister'),
    path('signup', views.postRegister, name='postRegister'),
    path('logout', views.userLogout, name='logout'),
    path('update', views.getuserupdate, name='getuserupdate'),
    path('edit', views.postuserupdate, name='postuserupdate'),

]
