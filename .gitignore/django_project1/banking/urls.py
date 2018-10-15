from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views as user_views

urlpatterns = [

	url(r'^register/',user_views.register, name='register'),
    url(r'^login/', user_views.login, name='login'),
    url(r'^logout/', user_views.logout, name='logout'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^checksession/', user_views.check_session, name = 'check_session'),
    url(r'^get_balance/', user_views.get_balance, name = 'get_balance'),
    url(r'^withdraw/', user_views.withdraw, name = 'withdraw'),
    url(r'^delete/', user_views.delete, name = 'delete'),
    url(r'^deposit/', user_views.deposit, name = 'deposit')
    
]