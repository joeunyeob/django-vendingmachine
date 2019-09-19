from django.conf.urls import include, url
from django.contrib import admin
from CRUD_Prac.views import UserCreateView, UserCreateDoneTV
from . import views

urlpatterns = [
    url(r'^$', views.index_redirect, name='index_redirect'),
    url(r'^VendingMachine/', include('VendingMachine.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('allauth.urls'))
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

]
