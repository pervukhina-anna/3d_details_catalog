"""
URL configuration for vsm_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from vsm_site import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # url-API
    path('api/v1/details/', DetailAPIView.as_view()),
    path('api/v1/create_detail/', CreateDetailAPIView.as_view()),
    path('api/v1/details/<int:pk>/', SingleDetailAPIView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    #url-сайта
    # path('', login_user, name='login_user'),

    path('', LoginUser.as_view(), name='login_user_2'),
    path('login_operator_2/', LoginOperator.as_view(), name='login_operator_2'),
    # path('logout/', logout_user, name='logout_2'),
    # path('login_operator/', login_operator, name='login_operator'),

    path('main_page_user/', main_page_user, name='main_page_user'),
    path('main_page_operator/', main_page_operator, name='main_page_operator'),
    path('detail_page/<int:detail_id>', detail_page, name='detail_page'),
    path('add_page/', add_page, name='add_page'),
    path('add_page_2/', add_page_2, name='add_page_2'),

    path('make_order/', make_order, name='make_order'),

    path('search/', search_view, name='search'),

    path('basket/', basket, name='basket'),
    path('basket_complete', basket_complete, name='basket_complete'),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
