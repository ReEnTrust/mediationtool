from django import forms


class UserForm(forms.Form):
    age = forms.BooleanField(label='Age')
    gender = forms.BooleanField(label='Gender')
    ALGO_CHOICES = [
        (1, 'Algorithm 1'),
        (2, 'Algorithm 2'),
        (3, 'Algorithm 3'),
    ]
    algo = forms.ChoiceField(choices = ALGO_CHOICES, label="algo", widget=forms.RadioSelect, required=True)


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
 
