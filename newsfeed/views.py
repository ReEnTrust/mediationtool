#import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .forms import ApproveFormA
from .forms import ApproveFormB
from .forms import ApproveFormC
from .forms import ApproveFormD
from .forms import LogForm
from .forms import ChangeVoteForm
from .forms import MediationForm

from .models import News
#from .models import Configuration
from .models import LogInstance
from .models import LogAction
from .models import AlgoChoice
# Create your views here.

#all_config = Configuration.all_config.all()

# config = age, gender, algoA, algoB, algoC
current_config=[True,True,True,True,True]

def concern_phrasing(string):
    if string=='I don\'t know':
        return 'don\'t know whether you would mind'
    if string=='Strongly disagree':
        return 'strongly disagree you would mind'
    if string=='Disagree':
        return 'disagree you would mind'
    if string=='No preference':
        return 'neither agree or disagree you would mind'
    if string=='Agree':
        return 'agree you would mind'
    if string=='Strongly agree':
        return 'strongly agree you would mind'

def slider_num_to_string(num):
    if num==0:
        return 'I don\'t know'
    if num==1:
        return 'Strongly disagree'
    if num==2:
        return 'Disagree'
    if num==3:
        return 'No preference'
    if num==4:
        return 'Agree'
    if num==5:
        return 'Strongly agree'

class IndexView(View):
    def get(self, request):
        context={}
        return render(request, 'newsfeed/index.html', context)

    def post(self, request):
        form = LogForm(data = request.POST)
        if form.is_valid():
            #algo = ''
            dataInstance = form.cleaned_data.get('dataInstance')
            #choice_algo = form.cleaned_data.get('algo')
            inst = LogInstance.all_instance.filter(log_identification_string=dataInstance).first()
            if not inst:
                newLogInstance = LogInstance(log_identification_string=dataInstance)
                newLogInstance.save()
            else:
                newLogInstance = inst
#            ans1_1 = slider_num_to_string(form.cleaned_data.get('qu1_1'))
#            ans1_2 = slider_num_to_string(form.cleaned_data.get('qu1_2'))
#            ans1_3 = slider_num_to_string(form.cleaned_data.get('qu1_3'))

            algoAconcern = slider_num_to_string(form.cleaned_data.get('algoAconcern'))
            #form1.cleaned_data.get('algoAconcern')
            algoBconcern = slider_num_to_string(form.cleaned_data.get('algoBconcern'))
            algoCconcern = slider_num_to_string(form.cleaned_data.get('algoCconcern'))
            algoDconcern = slider_num_to_string(form.cleaned_data.get('algoDconcern'))

            newLogInstance.concern_algo('A',algoAconcern)
            newLogInstance.concern_algo('B',algoBconcern)
            newLogInstance.concern_algo('C',algoCconcern)
            newLogInstance.concern_algo('D',algoDconcern)

#            newLogInstance.set_qu1(ans1_1,ans1_2,ans1_3)

        print(form.errors)

        return redirect('analyse', DataInstance=dataInstance)


class AnalyseView(View):
    def get(self, request, DataInstance):
        newsA = News.all_news.filter(algo = 'A')
        newsB = News.all_news.filter(algo = 'B')
        newsC = News.all_news.filter(algo = 'C')
        newsD = News.all_news.filter(algo = 'D')
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        all_votes = inst.all_votes_done()
        doneA = inst.done_A()
        doneB = inst.done_B()
        doneC = inst.done_C()
        doneD = inst.done_D()
        context={'all_newsA': newsA[0:3],'all_newsB': newsB[0:3],'all_newsC': newsC[0:3],'all_newsD': newsD[0:3], 'all_votes': all_votes, 'doneA': doneA, 'doneB': doneB, 'doneC': doneC, 'doneD': doneD}
        return render(request, 'newsfeed/analyse.html', context)

    def post(self,request, DataInstance):
        formA = ApproveFormA(data = request.POST)
        formB = ApproveFormB(data = request.POST)
        formC = ApproveFormC(data = request.POST)
        formD = ApproveFormD(data = request.POST)
#        instance = request.POST.__getitem__('data-instance')
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()

#        activated_config = inst.get_current_config()
#        algo_choice = inst.get_current_algo()
        if formA.is_valid():
            approvedA = formA.cleaned_data.get('approveA')
            algo_choiceA = AlgoChoice.all_choices.filter(algo='A').first()
            commentA = formA.cleaned_data.get('commentA')
            if approvedA=="yes":
                #print("yes")
                algo_choiceA.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceA.get_name(), log_comment = commentA)
                NewLogAction.save()
                inst.vote_algo('A','yes')
                inst.comment_algo('A',commentA)
            if approvedA=="no":
                #print("no")
                algo_choiceA.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceA.get_name(), log_comment = commentA)
                NewLogAction.save()
                inst.vote_algo('A','no')
                inst.comment_algo('A',commentA)
        if formB.is_valid():
            approvedB = formB.cleaned_data.get('approveB')
            algo_choiceB = AlgoChoice.all_choices.filter(algo='B').first()
            commentB = formB.cleaned_data.get('commentB')
            if approvedB=="yes":
                #print("yes")
                algo_choiceB.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceB.get_name(), log_comment = commentB)
                NewLogAction.save()
                inst.vote_algo('B','yes')
                inst.comment_algo('B',commentB)
            if approvedB=="no":
                #print("no")
                algo_choiceB.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceB.get_name(), log_comment = commentB)
                NewLogAction.save()
                inst.vote_algo('B','no')
                inst.comment_algo('B',commentB)
        if formC.is_valid():
            approvedC = formC.cleaned_data.get('approveC')
            algo_choiceC = AlgoChoice.all_choices.filter(algo='C').first()
            commentC = formC.cleaned_data.get('commentC')
            if approvedC=="yes":
                #print("yes")
                algo_choiceC.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceC.get_name(), log_comment = commentC)
                NewLogAction.save()
                inst.vote_algo('C','yes')
                inst.comment_algo('C',commentC)
            if approvedC=="no":
                #print("no")
                algo_choiceC.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceC.get_name(), log_comment = commentC)
                NewLogAction.save()
                inst.vote_algo('C','no')
                inst.comment_algo('C',commentC)
        if formD.is_valid():
            approvedD = formD.cleaned_data.get('approveD')
            algo_choiceD = AlgoChoice.all_choices.filter(algo='D').first()
            commentD = formD.cleaned_data.get('commentD')
            if approvedD=="yes":
                #print("yes")
                algo_choiceD.approve()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "yes", log_config = algo_choiceD.get_name(), log_comment = commentD)
                NewLogAction.save()
                inst.vote_algo('D','yes')
                inst.comment_algo('D',commentD)
            if approvedD=="no":
                #print("no")
                algo_choiceD.unapprove()
                NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "no", log_config = algo_choiceD.get_name(), log_comment = commentD)
                NewLogAction.save()
                inst.vote_algo('D','no')
                inst.comment_algo('D',commentD)
        return redirect('analyse', DataInstance)




class VotesView(View):
    def get(self, request, DataInstance):
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        list_yes=inst.get_list_yes()
        list_no=inst.get_list_no()

        for elt in list_yes:
            inst.set_shown_percentage(elt.get_name(),elt.like_ratio())
        for elt in list_no:
            inst.set_shown_percentage(elt.get_name(),elt.dislike_ratio())

        context={'config_yes': list_yes, 'config_no': list_no}
        return render(request, 'newsfeed/votes.html', context)

    def post(self, request, DataInstance):
        form1 = ChangeVoteForm(data = request.POST)
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        if form1.is_valid():
            NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "votes page questionnaire completed")
            NewLogAction.save()
            algoAchange = slider_num_to_string(form1.cleaned_data.get('algoAchange'))
            #form1.cleaned_data.get('algoAchange')
            algoBchange = slider_num_to_string(form1.cleaned_data.get('algoBchange'))
            algoCchange = slider_num_to_string(form1.cleaned_data.get('algoCchange'))
            algoDchange = slider_num_to_string(form1.cleaned_data.get('algoDchange'))
            inst.change_vote_algo('A',algoAchange)
            inst.change_vote_algo('B',algoBchange)
            inst.change_vote_algo('C',algoCchange)
            inst.change_vote_algo('D',algoDchange)
#            if algoAchange:
#                inst.change_vote_algo('A','yes')
#            else:
#                inst.change_vote_algo('A','no')
#            if algoBchange:
#                inst.change_vote_algo('B','yes')
#            else:
#                inst.change_vote_algo('B','no')
#            if algoCchange:
#                inst.change_vote_algo('C','yes')
#            else:
#                inst.change_vote_algo('C','no')
#            if algoDchange:
#                inst.change_vote_algo('D','yes')
#            else:
#                inst.change_vote_algo('D','no')




        return redirect('mediation', DataInstance)


class MediationView(View):
    def get(self, request, DataInstance):
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
#        nb_inst = LogInstance.all_instance.count()
#        initA = inst.get_opinion('A')
#        initB = inst.get_opinion('B')
#        initC = inst.get_opinion('C')
#        initD = inst.get_opinion('D')

        list_yes=inst.get_list_yes()
        list_no=inst.get_list_no()

        yesA = inst.yes('A')
        yesB = inst.yes('B')
        yesC = inst.yes('C')
        yesD = inst.yes('D')

        noA = inst.no('A')
        noB = inst.no('B')
        noC = inst.no('C')
        noD = inst.no('D')

        concernA=inst.get_concern('A')
        concernB=inst.get_concern('B')
        concernC=inst.get_concern('C')
        concernD=inst.get_concern('D')

        commentA=inst.get_comment('A')
        commentB=inst.get_comment('B')
        commentC=inst.get_comment('C')
        commentD=inst.get_comment('D')

#        nb_inst = LogInstance.all_instance.filter(vote_algoA = 'yes').exclude(log_identification_string = inst.get_name()).count()
#        comment_proA=LogInstance.all_instance.filter(vote_algoA = 'yes').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('A')
#        nb_inst = LogInstance.all_instance.filter(vote_algoA = 'no').exclude(log_identification_string = inst.get_name()).count()
#        comment_consA=LogInstance.all_instance.filter(vote_algoA = 'no').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('A')
#        nb_inst = LogInstance.all_instance.filter(vote_algoB = 'yes').exclude(log_identification_string = inst.get_name()).count()
#        comment_proB=LogInstance.all_instance.filter(vote_algoB = 'yes').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('B')
#        nb_inst = LogInstance.all_instance.filter(vote_algoB = 'no').exclude(log_identification_string = inst.get_name()).count()
#        comment_consB=LogInstance.all_instance.filter(vote_algoB = 'no').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('B')
#        nb_inst = LogInstance.all_instance.filter(vote_algoC = 'yes').exclude(log_identification_string = inst.get_name()).count()
#        comment_proC=LogInstance.all_instance.filter(vote_algoC = 'yes').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('C')
#        nb_inst = LogInstance.all_instance.filter(vote_algoC = 'no').exclude(log_identification_string = inst.get_name()).count()
#        comment_consC=LogInstance.all_instance.filter(vote_algoC = 'no').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('C')
#        nb_inst = LogInstance.all_instance.filter(vote_algoD = 'yes').exclude(log_identification_string = inst.get_name()).count()
#        comment_proD=LogInstance.all_instance.filter(vote_algoD = 'yes').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('D')
#        nb_inst = LogInstance.all_instance.filter(vote_algoD = 'no').exclude(log_identification_string = inst.get_name()).count()
#        comment_consD=LogInstance.all_instance.filter(vote_algoD = 'no').exclude(log_identification_string = inst.get_name())[random.randint(0,nb_inst-1)].get_comment('D')

        comment_proA = "Cookies allow platforms to collect information about users\' habits when they browse online. They also give access to browsing history, which makes the platform content accurate and up to date regarding what users are interested in at the moment."

        comment_consA = "When we accept cookies, our activity on the Internet tends to be tracked in order to collect as much data as possible. These data can be used to recommend the most relevant content (newsfeed, shopping online, etc). However, users don\'t have a guarantee to control what happens to these data. For example, platforms might sell this data to other companies."

        comment_proB = "Creating an account is generally the best way to have the most personalised content. It is also very useful for the platform to collect such data so they can train their newsfeed to recommend the best items to their users."

        comment_consB = "When we create an account, we have to fill in several fields that contain personal information. For example, websites often require us to give our name and date of birth. This is no problem for many people but sometimes users want to keep such information private or don't think the platform needs this data to provide its basic functionality."

        comment_proC = "When location is shared, content can be adapted to your profile based on where you are at the moment, or what people close to your location are interested in. This can also help exclude content not relevant to your area or country that you might not be interested in."

        comment_consC = "When we are asked to share location with a web site, we are sharing information about our current location we might not want them to have. We also might be shown less diverse content. For example, we might not see news relevant to other parts of the world."

        comment_proD = "Sponsored items are very important for platforms: most of the time, their business model relies on advertisement, which is necessary to keep offering their service for free. Without such advertisement, many online platforms would only be available for a subscription fee."

        comment_consD = "Sponsored items suggest information that is biased towards what an advertiser wants to show the user. This commercial interest might affect the neutrality of the information shown."

        concernA = concern_phrasing(inst.get_concern2('A'))
        concernB = concern_phrasing(inst.get_concern2('A'))
        concernC = concern_phrasing(inst.get_concern2('A'))
        concernD = concern_phrasing(inst.get_concern2('A'))

        context={'config_yes': list_yes, 'config_no': list_no, 'concernA':concernA, 'concernB':concernB, 'concernC': concernC, 'concernD':concernD, 'yesA':yesA, 'yesB' : yesB, 'yesC': yesC, 'yesD' : yesD, 'noA':noA, 'noB': noB, 'noC':noC, 'noD' : noD, 'commA': commentA, 'commB': commentB, 'commC': commentC, 'commD': commentD, 'comment_proA' : comment_proA, 'comment_proB' : comment_proB, 'comment_proC' : comment_proC, 'comment_proD' : comment_proD, 'comment_consA' : comment_consA, 'comment_consB' : comment_consB, 'comment_consC' : comment_consC, 'comment_consD' : comment_consD, 'concernA':concernA,'concernB':concernB,'concernC':concernC,'concernD':concernD}

        return render(request, 'newsfeed/mediation.html', context)

    def post(self, request, DataInstance):
        form1 = MediationForm(data = request.POST)
        inst = LogInstance.all_instance.filter(log_identification_string=DataInstance).first()
        if form1.is_valid():
            NewLogAction = LogAction(log_instance_name = DataInstance,log_action_description = "mediation page questionnaire completed")
            NewLogAction.save()
            algoAchangeConcern = slider_num_to_string(form1.cleaned_data.get('algoAchangeConcern'))
            #form1.cleaned_data.get('algoAchange')
            algoBchangeConcern = slider_num_to_string(form1.cleaned_data.get('algoBchangeConcern'))
            algoCchangeConcern = slider_num_to_string(form1.cleaned_data.get('algoCchangeConcern'))
            algoDchangeConcern = slider_num_to_string(form1.cleaned_data.get('algoDchangeConcern'))
            inst.change_concern_algo('A',algoAchangeConcern)
            inst.change_concern_algo('B',algoBchangeConcern)
            inst.change_concern_algo('C',algoCchangeConcern)
            inst.change_concern_algo('D',algoDchangeConcern)

            inst.set_comment_mediation(3,form1.cleaned_data.get('comment_tool'))
            inst.set_comment_mediation(4,form1.cleaned_data.get('comment_features'))

            confident = slider_num_to_string(form1.cleaned_data.get('confident'))
            informed = slider_num_to_string(form1.cleaned_data.get('informed'))
            incontrol = slider_num_to_string(form1.cleaned_data.get('incontrol'))
            positive = slider_num_to_string(form1.cleaned_data.get('positive'))
            inst.set_perception('confident',confident)
            inst.set_perception('informed',informed)
            inst.set_perception('incontrol',incontrol)
            inst.set_perception('positive',positive)

        return redirect('exit')

class ExitView(View):
    def get(self, request):
        context={}
        return render(request, 'newsfeed/exit.html', context)

