from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index, name='index'),
    path('result.html',views.result, name='result'),
    path('privacy.html',views.privacy, name='privacy'),
    path('transparency.html',views.transparency, name='transparency'),
]
