from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    context={}
    template = loader.get_template('newsfeed/index.html')
    return HttpResponse(template.render(context,request))

def simple_page(request):
    context={}
    template = loader.get_template('newsfeed/simple_page.html')
    return HttpResponse(template.render(context,request))

def shortcodes(request):
    context={}
    template = loader.get_template('newsfeed/shortcodes.html')
    return HttpResponse(template.render(context,request))
