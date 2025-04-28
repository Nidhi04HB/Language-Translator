from django.urls import path 
from .views import *
  
urlpatterns = [ 
    path('',home,name="home"), 
     path('translate/', translate_text, name='translate'),
]