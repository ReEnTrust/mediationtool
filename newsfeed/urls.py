from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index.html',views.index, name='index'),
    path('result.html',views.result, name='result'),
    path('privacy.html',views.privacy, name='privacy'),
    path('transparency.html',views.transparency, name='transparency'),
    path('personal.html',views.transparency, name='personal'),
    path('consensus.html',views.transparency, name='consensus'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
