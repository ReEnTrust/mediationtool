from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import News
from .models import Configuration

# Create your views here.



def index(request):
    context={}
    template = loader.get_template('newsfeed/index.html')
    return HttpResponse(template.render(context,request))

def result(request):
    all_news = News.all_news.all()
#    all_config = Configuration._instances
#    activated_config = all_config[0]
#    for config in all_config:
#        if config.is_activated():
#            activated_config = config
#    context={'all_news': all_news[0:3], 'config': activated_config}
    context={'all_news': all_news[0:3]}
    template = loader.get_template('newsfeed/result.html')
    return HttpResponse(template.render(context,request))

def privacy(request):
#    all_config = Configuration.all()
#    for config in all_config:
#        if config.is_activated():
#            activated_config = config
    context={}
    template = loader.get_template('newsfeed/privacy.html')
    return HttpResponse(template.render(context,request))

def transparency(request):
#    all_config = Configuration.all()
#    for config in all_config:
#        if config.is_activated():
#            activated_config = config
    context={}
    template = loader.get_template('newsfeed/transparency.html')
    return HttpResponse(template.render(context,request))

def personal(request):
    context={}
    template = loader.get_template('newsfeed/personal.html')
    return HttpResponse(template.render(context,request))

def consensus(request):
    context={}
    template = loader.get_template('newsfeed/consensus.html')
    return HttpResponse(template.render(context,request))
