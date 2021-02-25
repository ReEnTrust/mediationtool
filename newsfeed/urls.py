from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index.html',views.IndexView.as_view(), name='index'),
#    path('<DataInstance>/result.html',views.ResultView.as_view(), name='result'),
    path('<DataInstance>/analyse.html',views.AnalyseView.as_view(), name='analyse'),
#    path('<DataInstance>/privacy.html',views.PrivacyView.as_view(), name='privacy'),
#    path('<DataInstance>/transparency.html',views.TransparencyView.as_view(), name='transparency'),
    path('<DataInstance>/votes.html',views.VotesView.as_view(), name='votes'),
#    path('<DataInstance>/settings.html',views.SettingsView.as_view(), name='settings'),
    path('<DataInstance>/mediation.html',views.MediationView.as_view(), name='mediation'),
#    path('result.html',views.ResultView.as_view(), name='result'),
#    path('privacy.html',views.PrivacyView.as_view(), name='privacy'),
#    path('transparency.html',views.TransparencyView.as_view(), name='transparency'),
#    path('personal.html',views.TransparencyView.as_view(), name='personal'),
#    path('consensus.html',views.ConsensusView.as_view(), name='consensus'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
