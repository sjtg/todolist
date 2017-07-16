from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',

    url(r'^$', views.HomePage, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add/$', views.add, name="add"),
)
