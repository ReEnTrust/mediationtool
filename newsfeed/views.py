from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    context={}
    template = loader.get_template('newsfeed/index.html')
    return HttpResponse(template.render(context,request))

def result(request):
    context={}
    template = loader.get_template('newsfeed/result.html')
    return HttpResponse(template.render(context,request))

def privacy(request):
    context={}
    template = loader.get_template('newsfeed/privacy.html')
    return HttpResponse(template.render(context,request))

def transparency(request):
    context={}
    template = loader.get_template('newsfeed/transparency.html')
    return HttpResponse(template.render(context,request))

def consensus(request):
    context={}
    template = loader.get_template('newsfeed/consensus.html')
    return HttpResponse(template.render(context,request))
