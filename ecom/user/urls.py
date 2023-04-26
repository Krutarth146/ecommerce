from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/',Register,name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/', logout_view, name='logout'),
]