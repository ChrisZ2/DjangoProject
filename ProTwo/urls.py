from django.conf.urls import url
from ProTwo import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
]