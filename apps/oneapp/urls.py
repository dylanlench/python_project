from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logandreg),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^main$', views.main),

]