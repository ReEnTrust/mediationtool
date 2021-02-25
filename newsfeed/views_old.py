from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .forms import UserFormPrivacy
from .forms import UserFormTransparency
from .forms import ApproveForm
from .forms import LogForm
from .forms import SettingsForm

from .models import News
from .models import Configuration
from .models import LogInstance
from .models import LogAction
from .models import AlgoChoice
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
            algo = ''
            dataInstance = form.cleaned_data.get('dataInstance')
            #choice_algo = form.cleaned_data.get('algo')
            algoA = form.cleaned_data.get('algoA')
            algoB = form.cleaned_data.get('algoB')
            algoC = form.cleaned_data.get('algoC')
            algoD = form.cleaned_data.get('algoD')
            if algoA:
                algo = algo+'A'
            else:
                algo = algo+'_'
            if algoB:
                algo = algo+'B'
            else:
                algo = algo+'_'
            if algoC:
                algo = algo+'C'
            else:
                algo = algo+'_'
            if algoD:
                algo = algo+'D'
            else:
                algo = algo+'_'
        print(form.errors)
        newLogInstance = LogInstance(log_identification_string=dataInstance,initial_algo=algo)
        newLogInstance.set_config(algoA,algoB,algoC,algoD)
        newLogInstance.set_default_algo()
        newLogInstance.save()
        return redirect('mediation', DataInstance=dataInstance)


class MediationView(View):
    def get(self, request, DataInstance):
#        inst = LogInstance.all_instance.filter(log_identification_string = DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
        newsA = News.all_news.filter(algo = 'A')
        newsB = News.all_news.filter(algo = 'B')
        newsC = News.all_news.filter(algo = 'C')
        newsD = News.all_news.filter(algo = 'D')
        context={'all_newsA': newsA[0:3],'all_newsB': newsB[0:3],'all_newsC': newsC[0:3],'all_newsD': newsD[0:3]}
        return render(request, 'newsfeed/mediation.html', context)

    def post(self,request, DataInstance):
        form = ApproveForm(data = request.POST)
#        instance = request.POST.__getitem__('data-instance')
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
#        activated_config = inst.get_current_config()
#        algo_choice = inst.get_current_algo()
        if form.is_valid():
            approvedA = form.cleaned_data.get('approveA')
            approvedB = form.cleaned_data.get('approveB')
            approvedC = form.cleaned_data.get('approveC')
            approvedD = form.cleaned_data.get('approveD')
            algo_choiceA = AlgoChoice.all_choices.filter(algo='A').first()
            algo_choiceB = AlgoChoice.all_choices.filter(algo='B').first()
            algo_choiceC = AlgoChoice.all_choices.filter(algo='C').first()
            algo_choiceD = AlgoChoice.all_choices.filter(algo='D').first()
            comment = request.POST['comment'] #form.cleaned_data.get('comment')
            #print(comment)
            if approvedA=="yes":
                #print("yes")
                algo_choiceA.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceA, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('A','yes')
                inst.comment_algo('A',comment)
            if approvedA=="no":
                #print("no")
                algo_choiceA.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceA, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('A','no')
                inst.comment_algo('A',comment)

            if approvedB=="yes":
                #print("yes")
                algo_choiceB.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceB, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('B','yes')
                inst.comment_algo('B',comment)
            if approvedB=="no":
                #print("no")
                algo_choiceB.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceB, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('B','no')
                inst.comment_algo('B',comment)

            if approvedC=="yes":
                #print("yes")
                algo_choiceC.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceC, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('C','yes')
                inst.comment_algo('C',comment)
            if approvedC=="no":
                #print("no")
                algo_choiceC.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceC, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('C','no')
                inst.comment_algo('C',comment)

            if approvedD=="yes":
                #print("yes")
                algo_choiceD.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceD, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('D','yes')
                inst.comment_algo('D',comment)
            if approvedD=="no":
                #print("no")
                algo_choiceD.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceD, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo('D','no')
                inst.comment_algo('D',comment)
        return redirect('mediation', DataInstance)

class ResultView(View):
    def get(self, request, DataInstance):
#        all_news = News.all_news.all()
#        all_config = Configuration.all_config.all()
#        all_instances = LogInstance.all_instance.all()
        inst = LogInstance.all_instance.filter(log_identification_string = DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
                #print("result get method")
                #activated_config.print_config("!!! in result view")

#        for n in all_news:
#            if n.fit_config(current_config):
#                news.append(n)

#        activated_config = inst.get_current_config()
        algo_choice = inst.get_current_algo()
        algoA = False
        algoB = False
        algoC = False
        algoD = False
        if algo_choice.get_algo()=='A':
            algoA = True
        if algo_choice.get_algo()=='B':
            algoB = True
        if algo_choice.get_algo()=='C':
            algoC = True
        if algo_choice.get_algo()=='D':
            algoD = True
        #news = News.all_news.filter(algoA = activated_config.get_algoA(),algoB = activated_config.get_algoB(),algoC = activated_config.get_algoC(),algoD = activated_config.get_algoD())
        #activated_config.print_config("!!! in result view")
        #context={'all_news': news[0:3], 'config_age': current_config[0], 'config_gender': current_config[1], 'config_algoA': current_config[2], 'config_algoB': current_config[3], 'config_algoC': current_config[4]}
        news = News.all_news.filter(algo = algo_choice.get_algo())
        context={'all_news': news[0:3], 'config_description': algo_choice.explanation(), 'config_algoA': algoA, 'config_algoB': algoB, 'config_algoC': algoC, 'config_algoD': algoD}
        return render(request, 'newsfeed/result.html', context)

    def post(self,request, DataInstance):
        form = ApproveForm(data = request.POST)
#        instance = request.POST.__getitem__('data-instance')
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
#        activated_config = inst.get_current_config()
        algo_choice = inst.get_current_algo()
        if form.is_valid():
            approved = form.cleaned_data.get('approve')
            comment = request.POST['comment'] #form.cleaned_data.get('comment')
            #print(comment)
            if approved=="yes":
                #print("yes")
                algo_choice.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choice, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo(algo_choice.get_algo(),'yes')
            if approved=="no":
                #print("no")
                algo_choice.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choice, log_comment = comment)
                NewLogAction.save()
                inst.vote_algo(algo_choice.get_algo(),'no')
            inst.comment_algo(algo_choice.get_algo(),comment)
        #approving_count+=1
        return redirect('result', DataInstance)

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
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
        if form.is_valid():
            privacy = form.cleaned_data.get('privacy')
#            if privacy=='age':
#                inst.change_current_config_privacy(True,False)
#                inst.save()
#            elif privacy=='gender':
#                inst.change_current_config_privacy(False,True)
#                inst.save()
#            elif privacy=='age_gender':
#                inst.change_current_config_privacy(True,True)
#                inst.save()
#            elif privacy=='no_info':
#                inst.change_current_config_privacy(False,False)
#                inst.save()

#            if age and not activated_config.age:
#                current_config[0]=True
#                activated_config=activated_config.change_config_age()
                #activated_config.save()
                #activated_config.print_config("age has been disabled")
#            if not age:
#                activated_config=activated_config.change_config_age()
                #activated_config.save()
#                current_config[0]=False
#            if gender and not activated_config.gender:
#                current_config[1]=True
#                activated_config=activated_config.change_config_gender()
#            if not gender:
#                current_config[1]=False
#                activated_config=activated_config.change_config_gender()

        return redirect('result', DataInstance)

class SettingsView(View):
    def get(self, request, DataInstance):
        #inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        #config = inst.get_current_config()
        context={}
        return render(request, 'newsfeed/settings.html', context)

    def post(self, request, DataInstance):
        form = SettingsForm(data = request.POST)
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
#        if form.is_valid():
#            algoA = form.cleaned_data.get('algoA')
#            algoB = form.cleaned_data.get('algoB')
#            algoC = form.cleaned_data.get('algoC')
#            algoD = form.cleaned_data.get('algoD')
#            inst.set_config(algoA,algoB,algoC,algoD)
#            inst.save()
        if form.is_valid():
            algo = form.cleaned_data.get('algo')
            if algo=="algoA":
                inst.set_algo(AlgoChoice.all_choices.filter(algo='A').first())
            if algo=="algoB":
                inst.set_algo(AlgoChoice.all_choices.filter(algo='B').first())
            if algo=="algoC":
                inst.set_algo(AlgoChoice.all_choices.filter(algo='C').first())
            if algo=="algoD":
                inst.set_algo(AlgoChoice.all_choices.filter(algo='D').first())
            inst.save()
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
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()

        if form.is_valid():
            algo = form.cleaned_data.get('algo')
            if algo=="algoA":
                inst.change_current_config_transparency(True,False,False)
            if algo=="algoB":
                inst.change_current_config_transparency(False,True,False)
            if algo=="algoC":
                inst.change_current_config_transparency(False,False,True)


        return redirect('result', DataInstance)



class PersonalView(View):
    def get(self, request, DataInstance):
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
        list_yes=inst.get_list_yes()
        list_no=inst.get_list_no()



        context={}
        all_config = Configuration.all_config.all()

        context={'all_config': all_config, 'config_yes': list_yes, 'config_no': list_no}
        return render(request, 'newsfeed/personal.html', context)

class ConsensusView(View):
    def get(self, request, DataInstance):
        all_config = Configuration.all_config.all()
        context={'all_config': all_config}

        return render(request, 'newsfeed/consensus.html', context)




