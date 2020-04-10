from django.conf.urls import url,include
from blog import views

urlpatterns = [

    url("^$",views.index1),
    url("^aticel/(?P<articel_id>[0-9]+)",views.aticel,name='aticel'),
    url("^page/(?P<articel_id>[0-9]+)",views.edit_page,name='page'),
    url("^page_action/$",views.edit_action,name='page_action'),

]