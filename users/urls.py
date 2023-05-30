from django.urls import path
from .views import *
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', sign_out, name='logout'),
]