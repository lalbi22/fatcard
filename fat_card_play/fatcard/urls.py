from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^02', views.index, name='index'),
    url(r'^03', views.ajax, name='ajax'),
    url(r'^$', views.cardpages, name='cardpages'),
    url(r'^play/$', views.card_devide, name='card_devide'),
    url(r'^01/', views.listdigits, name='listdigits'),
]