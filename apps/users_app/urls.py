from django.conf.urls import url
import views

urlpatterns = [
    
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users/new$', views.newUser),
    url(r'^users$', views.users)

]