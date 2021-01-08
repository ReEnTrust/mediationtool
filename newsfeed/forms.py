from django import forms


class UserFormPrivacy(forms.Form):
    age = forms.BooleanField(label='age', required=False)
    gender = forms.BooleanField(label='gender', required=False)

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
    approve = forms.ChoiceField(choices = APPROVE_CHOICES, label="approve", widget=forms.RadioSelect, required=True)

class LogForm(forms.Form):
    dataInstance = forms.CharField(label='DataInstance')


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
 
