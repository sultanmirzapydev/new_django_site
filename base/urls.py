from django.urls import path
# we need to import fucntions from  the views file
from . import views

urlpatterns = [
    path('', views.show, name='realtime'),
    
]