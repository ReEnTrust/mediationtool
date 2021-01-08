from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index.html',views.IndexView.as_view(), name='index'),
    path('result.html',views.ResultView.as_view(), name='result'),
    path('privacy.html',views.PrivacyView.as_view(), name='privacy'),
    path('transparency.html',views.TransparencyView.as_view(), name='transparency'),
    path('personal.html',views.TransparencyView.as_view(), name='personal'),
    path('consensus.html',views.ConsensusView.as_view(), name='consensus'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
