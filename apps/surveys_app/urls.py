from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys$', views.index),
    url(r'^surveys/new$', views.new)
]