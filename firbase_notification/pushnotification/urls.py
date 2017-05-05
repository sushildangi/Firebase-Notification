from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/$', views.pushCategory, name='Category'),
    url(r'^formdata$', views.sendData, name='formdata'),
    url(r'^category/cat_notify$', views.sendDataCat, name='cat_notify'),
    url(r'^thanks/$', views.thanksMethod, name='thanks'),
]
