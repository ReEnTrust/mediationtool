from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import View
from .forms import UserForm
from .forms import FeedbackForm
from .forms import LogForm

from .models import News
from .models import Configuration

# Create your views here.





class IndexView(View):
    def get(self, request):
        context={}
        return render(request, 'newsfeed/index.html', context)

class ResultView(View):
    def get(self, request):
        all_news = News.all_news.all()
        context={'all_news': all_news[0:3]}#, 'config': config}
        return render(request, 'newsfeed/result.html', context)

    def post(self, request):
        all_news = News.all_news.all()
        all_config = Configuration.all_config.all()
        activated_config = all_config[0]
        for config in all_config:
            if config.is_activated():
                activated_config = config
        context={'all_news': all_news[0:3], 'config': activated_config}
        return render(request, 'newsfeed/result.html', context)

#def view_test(request, pk):
#    Configuration.objects.filter(activated=True).unactivate()
#    return HttpResponseRedirect(request.GET.get('next'))


class PrivacyView(View):
    def get(self, request):
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
        context={}
        return render(request, 'newsfeed/privacy.html', context)

    def post(self, request): 
        form = UserForm(data = request.POST)
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
        if form.is_valid():
            age=form.cleaned_data.get('age')
            gender=form.cleaned_data.get('gender')
            if age:
                activated_config.change_config_age()
            if gender:
                activated_config.change_config_gender()
        return redirect('result.html', activated_config)

    def reset(self, request):
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
        context={}
        return render(request, 'newsfeed/privacy.html', context)


def transparency(request):
#    all_config = Configuration.all_config.all()
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
