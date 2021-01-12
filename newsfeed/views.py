from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import View
from .forms import UserFormPrivacy
from .forms import UserFormTransparency
from .forms import ApproveForm
from .forms import FeedbackForm
from .forms import LogForm

from .models import News
from .models import Configuration
from .models import LogInstance
from .models import LogAction

# Create your views here.

#all_config = Configuration.all_config.all()

# config = age, gender, algoA, algoB, algoC
current_config=[True,True,True,True,True]



class IndexView(View):
    def get(self, request):
        context={}
        return render(request, 'newsfeed/index.html', context)

    def post(self, request):
        form = LogForm(data = request.POST)
        if form.is_valid():
            dataInstance = form.cleaned_data.get('dataInstance')
        print(form.errors)
        newLogInstance = LogInstance(log_identification_string=dataInstance)
        newLogInstance.save()
        return redirect('result', DataInstance=dataInstance)

class ResultView(View):
    def get(self, request, DataInstance):
        all_news = News.all_news.all()
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
                #print("result get method")
                #activated_config.print_config("!!! in result view")                
        news = []
        for n in all_news:
            if n.fit_config(current_config):
                news.append(n)
        #activated_config.print_config("!!! in result view")
        #context={'all_news': news[0:3], 'config_age': current_config[0], 'config_gender': current_config[1], 'config_algoA': current_config[2], 'config_algoB': current_config[3], 'config_algoC': current_config[4]}
        context={'all_news': news[0:3], 'config_age': activated_config.age, 'config_gender': activated_config.gender, 'config_algoA': activated_config.algoA, 'config_algoB': activated_config.algoB, 'config_algoC': activated_config.algoC}
        return render(request, 'newsfeed/result.html', context)

    def post(self,request, DataInstance):
        form = ApproveForm(data = request.POST) 
        #instance = request.POST.__getitem__('data-instance')
        instance= DataInstance
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
        if form.is_valid():
            approved = form.cleaned_data.get('approve')
            comment = form.cleaned_data.get('comment')
            print(comment)
            if approved=="yes":
                print("yes")
                activated_config.approve()
                NewLogAction = LogAction(log_instance_id = instance,log_action_description = "yes", log_config = activated_config, log_comment = comment)
                NewLogAction.save()
            if approved=="no":
                print("no")
                activated_config.unapprove()
                NewLogAction = LogAction(log_instance_id = instance,log_action_description = "no", log_config = activated_config, log_comment = comment)
                NewLogAction.save()
        #approving_count+=1
        return redirect('personal', DataInstance)

#def view_test(request, pk):
#    Configuration.objects.filter(activated=True).unactivate()
#    return HttpResponseRedirect(request.GET.get('next'))


class PrivacyView(View):
    def get(self, request, DataInstance):
        #for config in all_config:
        #    if config.is_activated():
        #        activated_config = config
                #print("privacy get method")
                #activated_config.print_config()
        #config = all_config[0].get_activated_config()
        #config.print_config()
        context={}
        return render(request, 'newsfeed/privacy.html', context)

    def post(self, request, DataInstance): 
        form = UserFormPrivacy(data = request.POST)
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
        activated_config.print_config("before sending form")
        if form.is_valid():
            age=form.cleaned_data.get('age')
            gender=form.cleaned_data.get('gender')
            if age and not activated_config.age:
                current_config[0]=True
                activated_config=activated_config.change_config_age()
                #activated_config.save()                
                #activated_config.print_config("age has been disabled")
            if not age:           
                activated_config=activated_config.change_config_age()
                #activated_config.save() 
                current_config[0]=False
            if gender and not activated_config.gender:
                current_config[1]=True
                activated_config=activated_config.change_config_gender()
            if not gender:
                current_config[1]=False
                activated_config=activated_config.change_config_gender()

        return redirect('result', DataInstance)


class TransparencyView(View):
#    all_config = Configuration.all_config.all()
#    for config in all_config:
#        if config.is_activated():
#            activated_config = config
    def get(self, request, DataInstance):
        context={}
        return render(request, 'newsfeed/transparency.html', context)

    def post(self, request, DataInstance):
        form = UserFormTransparency(data = request.POST)
        all_config = Configuration.all_config.all()
        for config in all_config:
            if config.is_activated():
                activated_config = config
        
        if form.is_valid():
            algo = form.cleaned_data.get('algo')
            if algo=="algoA":
                activated_config=activated_config.change_config_algoA()
                current_config[2]=True
                current_config[3]=False
                current_config[4]=False
            if algo=="algoB":
                activated_config=activated_config.change_config_algoB()
                activated_config.print_config("algoB selected")
                current_config[2]=False
                current_config[3]=True
                current_config[4]=False
            if algo=="algoC":
                activated_config=activated_config.change_config_algoC()
                current_config[2]=False
                current_config[3]=False
                current_config[4]=True


        return redirect('result', DataInstance)
    


class PersonalView(View):
    def get(self, request, DataInstance):    
        context={}
        all_config = Configuration.all_config.all()
        list_yes=[]
        list_no=[]
        list_actions_instance = LogAction.objects.filter(log_instance_id = DataInstance)
        for action in list_actions_instance:
            if action.log_action_description=='yes':
                list_yes.append(action.log_config)
            else:
                list_no.append(action.log_config)
        context={'config_yes': list_yes, 'config_no': list_no}
        return render(request, 'newsfeed/personal.html', context)

class ConsensusView(View):
    def get(self, request, DataInstance):
        all_config = Configuration.all_config.all()
        context={'all_config': all_config}
        
        return render(request, 'newsfeed/consensus.html', context)




