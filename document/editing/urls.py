from django.contrib import admin
from django.urls import path
from editing.views import *

app_name = 'editing'

urlpatterns = [
    path('',index,name='index1'),
    path('download',download,name='download'),
    path('editing',editing,name='editing'),
    path('index',index,name='index'),
    #path('admin/', admin.site.urls),
]