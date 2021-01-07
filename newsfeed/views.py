from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import View
from .forms import UserFormPrivacy
from .forms import UserFormTransparency
from .forms import FeedbackForm
from .forms import LogForm

from .models import News
from .models import Configuration

# Create your views here.

#all_config = Configuration.all_config.all()

# config = age, gender, algoA, algoB, algoC
current_config=[True,True,True,True,True]

class IndexView(View):
    def get(self, request):
        context={}
        return render(request, 'newsfeed/index.html', context)

class ResultView(View):

    def get(self, request):
        all_news = News.all_news.all()
        #activated_config = all_config[0]
        #for config in all_config:
        #    if config.is_activated():
        #        activated_config = config
                #print("result get method")
                #activated_config.print_config()                
        news = []
        for n in all_news:
            if n.fit_config(current_config):
                news.append(n)
        context={'all_news': news[0:3], 'config_age': current_config[0], 'config_gender': current_config[1], 'config_algoA': current_config[2], 'config_algoB': current_config[3], 'config_algoC': current_config[4]}
        return render(request, 'newsfeed/result.html', context)

#def view_test(request, pk):
#    Configuration.objects.filter(activated=True).unactivate()
#    return HttpResponseRedirect(request.GET.get('next'))


class PrivacyView(View):
    def get(self, request):
        #for config in all_config:
        #    if config.is_activated():
        #        activated_config = config
                #print("privacy get method")
                #activated_config.print_config()
        #config = all_config[0].get_activated_config()
        #config.print_config()
        context={}
        return render(request, 'newsfeed/privacy.html', context)

    def post(self, request): 
        form = UserFormPrivacy(data = request.POST)
        #for config in all_config:
        #    if config.is_activated():
        #        activated_config = config
        #activated_config.print_config()
        if form.is_valid():
            age=form.cleaned_data.get('age')
            gender=form.cleaned_data.get('gender')
            if age:
                current_config[0]=True
                #activated_config=activated_config.change_config_age()
                #activated_config.print_config("age has been disabled")
            else:            
                current_config[0]=False
            if gender:
                current_config[1]=True
            else:
                current_config[1]=False
                #activated_config=activated_config.change_config_gender()
        #activated_config.print_config("config activated at this point")
        #for config in all_config:
        #    if config.is_activated():
        #        config.print_config("[!!!] privacy post method")
        return redirect('result.html')


class TransparencyView(View):
#    all_config = Configuration.all_config.all()
#    for config in all_config:
#        if config.is_activated():
#            activated_config = config
    def get(self,request):
        context={}
        return render(request, 'newsfeed/transparency.html', context)

    def post(self,request):
        form = UserFormTransparency(data = request.POST)
        if form.is_valid():
            algo = form.cleaned_data.get('algo')
            if algo=="algoA":
                current_config[2]=True
                current_config[3]=False
                current_config[4]=False
            if algo=="algoB":
                current_config[2]=False
                current_config[3]=True
                current_config[4]=False
            if algo=="algoC":
                current_config[2]=False
                current_config[3]=False
                current_config[4]=True


        return redirect('result.html')
    


def personal(request):
    context={}
    template = loader.get_template('newsfeed/personal.html')
    return HttpResponse(template.render(context,request))

def consensus(request):
    context={}
    template = loader.get_template('newsfeed/consensus.html')
    return HttpResponse(template.render(context,request))
