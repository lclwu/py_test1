"""del_number URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url("^xhqb_index/$",views.xhqb_index),
    # path('ad/', views.index),
    # path('add/', views.search_from),
    # path('search/', views.search),
    # path('search_post/', views.search_post),
    # path('mobler/', views.mobler_data),
    path('mobler_find/', views.mobler_find,name='mobler_find'),
    url('^page/',views.update_mobler,name='page'),
    url("^msg/",views.msg_find,name="msg")


]
