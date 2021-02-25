from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .forms import ApproveForm
from .forms import LogForm

from .models import News
#from .models import Configuration
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
#        newLogInstance.set_config(algoA,algoB,algoC,algoD)
#        newLogInstance.set_default_algo()
        newLogInstance.save()
        return redirect('analyse', DataInstance=dataInstance)


class AnalyseView(View):
    def get(self, request, DataInstance):
#        inst = LogInstance.all_instance.filter(log_identification_string = DataInstance).exclude(current_config = None).exclude(current_algo = None).first()
        newsA = News.all_news.filter(algo = 'A')
        newsB = News.all_news.filter(algo = 'B')
        newsC = News.all_news.filter(algo = 'C')
        newsD = News.all_news.filter(algo = 'D')
        context={'all_newsA': newsA[0:3],'all_newsB': newsB[0:3],'all_newsC': newsC[0:3],'all_newsD': newsD[0:3]}
        return render(request, 'newsfeed/analyse.html', context)

    def post(self,request, DataInstance):
        form = ApproveForm(data = request.POST)
#        instance = request.POST.__getitem__('data-instance')
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
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
        return redirect('analyse', DataInstance)




class VotesView(View):
    def get(self, request, DataInstance):
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        list_yes=inst.get_list_yes()
        list_no=inst.get_list_no()

        context={'config_yes': list_yes, 'config_no': list_no}
        return render(request, 'newsfeed/votes.html', context)

class MediationView(View):
    def get(self, request, DataInstance):
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        initA = False
        initB = False
        initC = False
        initD = False
        initial_opinion = inst.get_initial_algo()
        if initial_opinion[0]=='A':
            initA = True
        if initial_opinion[1]=='B':
            initA = True
        if initial_opinion[2]=='C':
            initA = True
        if initial_opinion[3]=='D':
            initA = True
        list_yes=inst.get_list_yes()
        list_no=inst.get_list_no()
        commentA=inst.get_comment('A')
        commentB=inst.get_comment('B')
        commentC=inst.get_comment('C')
        commentD=inst.get_comment('D')

        context={'config_yes': list_yes, 'config_no': list_no, 'commA': commentA, 'commB': commentB, 'commC': commentC, 'commD': commentD, 'initA': initA, 'initB': initB, 'initC': initC, 'initD': initD}

        return render(request, 'newsfeed/mediation.html', context)




