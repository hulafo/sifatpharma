from django.conf.urls import url,include
from . import views

urlpatterns = [
   
    url(r'^$',views.index,name='index'),
   url(r'^about/',views.about,name='about_en'),
    #url(r'^blog/',views.blog,name='blog'),
    url(r'^contact/',views.contact,name='contact_en'),

]
