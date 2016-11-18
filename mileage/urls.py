from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^do_login$', views.do_login, name='dologin'),
    url(r'^other$', views.other, name='other'),
    url(r'^poop$', views.poop, name='other'),
    url(r'^fillup$', views.list_fillup, name='fillups'),
    url(r'^fillup/new$', views.new_fillup, name='newfillup'),
    url(r'^fillup/save$', views.save_fillup, name='savefillup'),
]
