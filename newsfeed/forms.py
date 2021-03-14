from django import forms

class UserFormPrivacy(forms.Form):
#    age = forms.BooleanField(label='age', required=False)
#    gender = forms.BooleanField(label='gender', required=False)
    PRIVACY_CHOICES = [
        ('age', 'age'),
        ('gender', 'gender'),
        ('age_gender','age_gender'),
        ('no_info','no_info'),
    ]
    privacy = forms.ChoiceField(choices = PRIVACY_CHOICES, label="privacy", widget=forms.RadioSelect, required=True)

class UserFormTransparency(forms.Form):
    ALGO_CHOICES = [
        ('algoA', 'algoA'),
        ('algoB', 'algoB'),
        ('algoC', 'algoC'),
    ]
    algo = forms.ChoiceField(choices = ALGO_CHOICES, label="algo", widget=forms.RadioSelect, required=True)

class ApproveForm(forms.Form):
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveA = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveA", widget=forms.RadioSelect, required=False)
    approveB = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveB", widget=forms.RadioSelect, required=False)
    approveC = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveC", widget=forms.RadioSelect, required=False)
    approveD = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveD", widget=forms.RadioSelect, required=False)

    commentA = forms.CharField(widget=forms.Textarea, required=True)
    commentB = forms.CharField(widget=forms.Textarea, required=True)
    commentC = forms.CharField(widget=forms.Textarea, required=True)
    commentD = forms.CharField(widget=forms.Textarea, required=True)



class ApproveFormA(forms.Form):
    commentA = forms.CharField(widget=forms.Textarea, required=True)
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveA = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveA", widget=forms.RadioSelect, required=False)

class ApproveFormB(forms.Form):
    commentB = forms.CharField(widget=forms.Textarea, required=True)
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveB = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveB", widget=forms.RadioSelect, required=False)

class ApproveFormC(forms.Form):
    commentC = forms.CharField(widget=forms.Textarea, required=True)
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveC = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveC", widget=forms.RadioSelect, required=False)

class ApproveFormD(forms.Form):
    commentD = forms.CharField(widget=forms.Textarea, required=True)
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveD = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveD", widget=forms.RadioSelect, required=False)

class LogForm(forms.Form):
    dataInstance = forms.CharField(label='DataInstance')
#    ALGO_CHOICES = [
#        ('algoA', 'algoA'),
#        ('algoB', 'algoB'),
#        ('algoC', 'algoC'),
#        ('algoD', 'algoD'),
#    ]
#    algo = forms.ChoiceField(choices = ALGO_CHOICES, label="algo", widget=forms.RadioSelect, required=True)

#    qu1_1 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_qu1_1'}), label='qu1_1', required=True)
# qu1_2 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_qu1_2'}), label='qu1_2', required=True)
#    qu1_3 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_qu1_3'}), label='qu1_3', required=True)
    algoAconcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoAconcern'}), label='algoAconcern', required=True)
    #forms.BooleanField(label='algoAconcern', required=False)
    algoBconcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoBconcern'}), label='algoBconcern', required=True)
    #forms.BooleanField(label='algoBconcern', required=False)
    algoCconcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoCconcern'}), label='algoCconcern', required=True)
    #forms.BooleanField(label='algoCconcern', required=False)
    algoDconcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoDconcern'}), label='algoDconcern', required=True)
    #forms.BooleanField(label='algoDconcern', required=False)




class ChangeVoteForm(forms.Form):
#    ALGO_CHOICES = [
#        ('algoA', 'algoA'),
#        ('algoB', 'algoB'),
#        ('algoC', 'algoC'),
#        ('algoD', 'algoD'),
#    ]
#    algo = forms.ChoiceField(choices = ALGO_CHOICES, label="algo", widget=forms.RadioSelect, required=True)
    algoAchange = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoAchange'}), label='algoAchange', required=True)
    #forms.BooleanField(label='algoAchange', required=False)
    algoBchange = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoBchange'}), label='algoBchange', required=True)
    #forms.BooleanField(label='algoBchange', required=False)
    algoCchange = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoCchange'}), label='algoCchange', required=True)
    #forms.BooleanField(label='algoCchange', required=False)
    algoDchange = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoDchange'}), label='algoDchange', required=True)
    #forms.BooleanField(label='algoDchange', required=False)

#    ALGO_CHOICES = [
#        ('algoA', 'algoA'),
#        ('algoB', 'algoB'),
#        ('algoC', 'algoC'),
#        ('algoD', 'algoD'),
#    ]


class MediationForm(forms.Form):

    algoAchangeConcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoAchangeConcern'}), label='algoAchangeConcern', required=True)
    algoBchangeConcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoBchangeConcern'}), label='algoBchangeConcern', required=True)
    algoCchangeConcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoCchangeConcern'}), label='algoCchangeConcern', required=True)
    algoDchangeConcern = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_algoDchangeConcern'}), label='algoDchangeConcern', required=True)

    confident = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_confident'}), label='confident', required=True)
    informed = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_informed'}), label='informed', required=True)
    incontrol = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_incontrol'}), label='incontrol', required=True)
    positive = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '5', 'id':'id_confident'}), label='confident', required=True)

    comment_tool = forms.CharField(widget=forms.Textarea, required=True)
    comment_features = forms.CharField(widget=forms.Textarea, required=True)

class SettingsForm(forms.Form):
#    algoA = forms.BooleanField(label='algoA', required=False)
#    algoB = forms.BooleanField(label='algoB', required=False)
#    algoC = forms.BooleanField(label='algoC', required=False)
#    algoD = forms.BooleanField(label='algoD', required=False)

    ALGO_CHOICES = [
        ('algoA', 'algoA'),
        ('algoB', 'algoB'),
        ('algoC', 'algoC'),
        ('algoD', 'algoD'),
    ]
    algo = forms.ChoiceField(choices = ALGO_CHOICES, label="algo", widget=forms.RadioSelect, required=True)

class LogApproveForm(forms.Form):
    dataApprove = forms.CharField(label='DataApprove')

class FeedbackForm(forms.Form):
    comment= forms.CharField(widget=forms.Textarea, required=False)
    FEED_CHOICES = [
        (1, 'Totally disagree'),
        (2, 'Disagree'),
        (3, 'Neutral'),
        (4, 'I do not know'),
        (5, 'Agree'),
        (6, 'Totally agree'),
    ]
    feed = forms.ChoiceField(choices = FEED_CHOICES, label="feed", widget=forms.RadioSelect, required=False)









