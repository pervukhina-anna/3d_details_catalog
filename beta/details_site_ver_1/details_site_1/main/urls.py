from django.urls import path

from .views import *


urlpatterns = [
    path('', login),
    path('users/', user_show),
    path('registrate/', registrate, name='registrate'),
    #path('registrate/', RegisterUser.as_view(), name='register'),
    path('main_page/', main_page, name='main_page'),
    path('detail_page/', detail_page, name='detail_page'),
    path('basket/', detail_page, name='basket'),
]