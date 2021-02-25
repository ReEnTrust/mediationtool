import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    all_news = models.Manager()
    #num=models.IntegerField()
    #rating=models.FloatField()
    title=models.CharField(max_length=1000)
    #date=models.DateTimeField('date published')
    #author=models.CharField(max_length=40)
    category=models.CharField(max_length=50)
    body=models.CharField(max_length=5000)
    url=models.CharField(max_length=1000, default='')
    #default=models.BooleanField()
#    age=models.BooleanField()
#    gender=models.BooleanField()
    #algoA=models.BooleanField(default = 'False')
    #algoB=models.BooleanField(default = 'False')
    #algoC=models.BooleanField(default = 'False')
    #algoD=models.BooleanField(default = 'False')
    algo=models.CharField(max_length=1, default='')
    #selected_because=models.CharField(max_length = 5000, default = '')

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class AlgoChoice(models.Model):
    all_choices = models.Manager()
    algo=models.CharField(max_length=1, default='')
    approved=models.IntegerField(default=0)
    unapproved=models.IntegerField(default=0)
    total_votes=models.IntegerField(default=0)

    def __str__(self):
        return self.algo + " | approved: " + str(self.approved)+" | unapproved: "+str(self.unapproved)

    def isA(self):
        return self.algo=='A'

    def isB(self):
        return self.algo=='B'

    def isC(self):
        return self.algo=='C'

    def isD(self):
        return self.algo=='D'

    def get_algo(self):
        return self.algo


    def explanation(self):
        r = ""

        if self.algo=='B':
            r = r + "Algorithm B uses similar profiles to recommend adapted news: the result is based on what has been like by users that share demographic information with Alex in order to increase their chances to like it. It requires Alex to have an account on the platform so we can find suc similar users in our database."
        if self.algo=='A':
            r = r + "Algorithm A uses profile's history to recommend adapted news: the result is based on what pages Alex has visited and liked recently in order to propose similar items. It requires Alex to accept our functional cookies so we know better their activity online."
        if self.algo=='C':
            r = r + "Algorithm C uses location: if Alex accepts to share their current location with us, we will be able to provide news items that are close to them. It increases the chances for Alex to read and appreciate our content."
        if self.algo=='D':
            r = r + "Algorithm D does not use any personal information about Alex: in this case, we provide news items based on what is popular on our website and sponsorised news. It is important for our business model to show sponsorised content when it is relevant."
        return r

    def print_like_ratio(self):
        if self.total_votes==0:
            return "No like"
        else:
            return str(round(self.approved*100/self.total_votes))+"%"

    def print_dislike_ratio(self):
        if self.total_votes==0:
            return "No like"
        else:
            return str(round(self.unapproved*100/self.total_votes))+"%"

    def approve(self):
        self.approved+=1
        self.total_votes+=1
        #self.print_config("approve method")
        self.save()

    def unapprove(self):
        self.unapproved+=1
        self.total_votes+=1
        self.save()

class LogInstance(models.Model):
    all_instance = models.Manager()
    log_instance_creation_date = models.DateTimeField(auto_now_add=True)
    log_identification_string = models.CharField(max_length=200, default='not provided')

    initial_algo=models.CharField(max_length=4, default='____')
    vote_algoA = models.CharField(max_length=10, default='unknown')
    comment_algoA = models.CharField(max_length=2000, default='no comment')
    vote_algoB = models.CharField(max_length=10, default='unknown')
    comment_algoB = models.CharField(max_length=2000, default='no comment')
    vote_algoC = models.CharField(max_length=10, default='unknown')
    comment_algoC = models.CharField(max_length=2000, default='no comment')
    vote_algoD = models.CharField(max_length=10, default='unknown')
    comment_algoD = models.CharField(max_length=2000, default='no comment')



    def __str__(self):
        #return str(self.id)+" "+str(self.log_instance_creation_date)
        return self.log_identification_string+" | "+str(self.log_instance_creation_date)

    def set_algo(self,algo):
        self.current_algo = algo
        self.save()

    def vote_algo(self,algo,vote):
        if algo == 'A':
            self.vote_algoA = vote
        if algo == 'B':
            self.vote_algoB = vote
        if algo == 'C':
            self.vote_algoC = vote
        if algo == 'D':
            self.vote_algoD = vote
        self.save()

    def comment_algo(self,algo,comment):
        if algo == 'A':
            self.comment_algoA = comment
        if algo == 'B':
            self.comment_algoB = comment
        if algo == 'C':
            self.comment_algoC = comment
        if algo == 'D':
            self.comment_algoD = comment
        self.save()


    def get_log_instance(self,id_string):
        return LogInstance.all_instance.filter(log_identification_string = id_string).first()

    def get_list_yes(self):
        rslt = []
        if self.vote_algoA == 'yes':
            rslt.append(AlgoChoice.all_choices.filter(algo='A').first())
        if self.vote_algoB == 'yes':
            rslt.append(AlgoChoice.all_choices.filter(algo='B').first())
        if self.vote_algoC == 'yes':
            rslt.append(AlgoChoice.all_choices.filter(algo='C').first())
        if self.vote_algoD == 'yes':
            rslt.append(AlgoChoice.all_choices.filter(algo='D').first())
        return rslt

    def get_list_no(self):
        rslt = []
        if self.vote_algoA == 'no':
            rslt.append(AlgoChoice.all_choices.filter(algo='A').first())
        if self.vote_algoB == 'no':
            rslt.append(AlgoChoice.all_choices.filter(algo='B').first())
        if self.vote_algoC == 'no':
            rslt.append(AlgoChoice.all_choices.filter(algo='C').first())
        if self.vote_algoD == 'no':
            rslt.append(AlgoChoice.all_choices.filter(algo='D').first())
        return rslt

    def get_comment(self,algo):
        if algo == 'A':
            return self.comment_algoA
        if algo == 'B':
            return self.comment_algoB
        if algo == 'C':
            return self.comment_algoC
        if algo == 'D':
            return self.comment_algoD

    def get_initial_algo(self):
        return self.initial_algo

class LogAction(models.Model):
    log_action_date = models.DateTimeField(auto_now_add=True)
    log_instance_name = models.CharField(max_length=200, default='not provided')
    log_action_description = models.CharField(max_length=20)
    log_config = models.ForeignKey(AlgoChoice, on_delete=models.CASCADE)
    log_comment = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.log_instance_name)+"|"+str(self.log_action_description)+"|"+str(self.log_action_date)+"|"+str(self.log_config)+"|"+str(self.log_comment)


