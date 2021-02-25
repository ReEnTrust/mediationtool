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

class ApproveFormA(forms.Form):
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveA = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveA", widget=forms.RadioSelect, required=False)

class ApproveFormB(forms.Form):
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveB = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveB", widget=forms.RadioSelect, required=False)

class ApproveFormC(forms.Form):
    APPROVE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    approveC = forms.ChoiceField(choices = APPROVE_CHOICES, label="approveC", widget=forms.RadioSelect, required=False)

class ApproveFormD(forms.Form):
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
    algoA = forms.BooleanField(label='algoA', required=False)
    algoB = forms.BooleanField(label='algoB', required=False)
    algoC = forms.BooleanField(label='algoC', required=False)
    algoD = forms.BooleanField(label='algoD', required=False)

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

