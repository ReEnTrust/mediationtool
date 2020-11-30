from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index, name='index'),
    path('simple_page.html',views.simple_page, name='simple_page'),
    path('shortcodes.html',views.shortcodes, name='shortcodes'),
]
