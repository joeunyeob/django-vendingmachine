from django.conf.urls import url
from . import views


urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^buy/(?P<id>\d+)/(?P<count>\d+)$', views.buy, name='buy'),
    url(r'^charts/', views.get_data, name='charts'),
]
