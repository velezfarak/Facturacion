from django.urls import path
from .views import calendario
urlpatterns = [
    path('', calendario, name='calendario')
]