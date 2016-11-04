from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^other$', views.other, name='other'),
    url(r'^poop$', views.poop, name='other'),
]