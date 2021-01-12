import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    all_news = models.Manager()
    num=models.IntegerField()
    rating=models.FloatField()
    title=models.CharField(max_length=1000)
    date=models.DateTimeField('date published')
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=20)
    body=models.CharField(max_length=5000)
    default=models.BooleanField()
    age=models.BooleanField()
    gender=models.BooleanField()
    algoA=models.BooleanField()
    algoB=models.BooleanField()
    algoC=models.BooleanField()

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

    def fit_config(self, config):
        #return self.age==config.age and self.gender==config.gender and self.algoA==config.algoA and self.algoB == config.algoB and self.algoC == config.algoC
        return self.age==config[0] and self.gender==config[1] and (self.algoA==config[2] or self.algoB == config[3] or self.algoC == config[4])



class Configuration(models.Model):
#    _instances = []
    all_config = models.Manager()
    activated=models.BooleanField(default=True)
    age=models.BooleanField(default=True)
    gender=models.BooleanField(default=True)
    algoA=models.BooleanField(default=True)
    algoB=models.BooleanField(default=True)
    algoC=models.BooleanField(default=True)
    approved=models.IntegerField(default=0)
    unapproved=models.IntegerField(default=0)
    total_votes=models.IntegerField(default=0)


#    def __init__(self,a,g,alA,alB,alC):
#        Configuration._instances.append(self)
#        self.activated=True
#        self.age=a
#        self.gender=g
#        self.algoA=alA
#        self.algoB=alB
#        self.algoC=alC

    def print_config(self, s=""):
        print("print located in: "+s+"\nACTIVATED: "+str(self.activated)+"\n age: "+str(self.age)+", gender: "+str(self.gender)+", algoA: "+str(self.algoA)+", algoB: "+str(self.algoB)+", algoC: "+str(self.algoC)+" approval ratio:"+str(self.approved)+"/"+str(self.total_votes))

    def is_activated(self):
        return self.activated

    def activate(self):
        self.activated=True

    def unactivate(self):
        self.activated=False

    def approve(self):
        self.approved+=1
        self.total_votes+=1
        self.print_config("approve method")
        self.save()

    def unapprove(self):
        self.unapproved+=1
        self.total_votes+=1
        self.save()


    def get_activated_config(self):
        all_config = Configuration.all_config.all()
        c = all_config[0]
        for config in all_config:
            if config.is_activated():
                config.print_config("get activated config")
                c = config
        return c


    def change_config_age(self):
        for config in Configuration.all_config.all():
            if self.age!=config.age:
                if self.gender==config.gender:
                    if self.algoA==config.algoA:
                        if self.algoB==config.algoB:
                            if self.algoC==config.algoC:
                                config.activate()
                                self.unactivate()
                                config.save()
                                self.save()
                                return config

#        config=Configuration(not self.age, self.gender, self.algoA, self.algoB, self.algoC)
#        return config 

    def change_config_gender(self):
        for config in Configuration.all_config.all():
            if self.age==config.age:
                if self.gender!=config.gender:
                    if self.algoA==config.algoA:
                        if self.algoB==config.algoB:
                            if self.algoC==config.algoC:
                                config.activate()
                                self.unactivate()
                                config.print_config()
                                config.save()
                                self.save()
                                return config
                                
#        config=Configuration(self.age, not self.gender, self.algoA, self.algoB, self.algoC)
#        return config 

    def change_config_algoA(self):
        for config in Configuration.all_config.all():
            if self.age==config.age:
                if self.gender==config.gender:
                    if self.algoA!=config.algoA:
                        config.activate()
                        self.unactivate()
                        config.save()
                        self.save()
                        return config
#        config=Configuration(self.age, self.gender, not self.algoA, self.algoB, self.algoC)
#        return config 

    def change_config_algoB(self):
        for config in Configuration.all_config.all():
            if self.age==config.age:
                if self.gender==config.gender:
                    if self.algoB!=config.algoB:
                        config.activate()
                        self.unactivate()
                        config.save()
                        self.save()
                        print("ALGO CHANGED FOR B")
                        return config
#        config=Configuration(self.age, self.gender, self.algoA, not self.algoB, self.algoC)
#        return config 

    def change_config_algoC(self):
        for config in Configuration.all_config.all():
            if self.age==config.age:
                if self.gender==config.gender:
                    if self.algoC!=config.algoC:
                        config.activate()
                        self.unactivate()
                        config.save()
                        self.save()
                        return config
#        config=Configuration(self.age, self.gender, self.algoA, self.algoB, not self.algoC)
#        return config 


class LogInstance(models.Model):
    log_instance_creation_date = models.DateTimeField(auto_now_add=True)
    log_identification_string = models.CharField(max_length=200, default='not provided')

    def __str__(self):
        return str(self.id)+" "+str(self.log_instance_creation_date)


class LogAction(models.Model):
    log_action_date = models.DateTimeField(auto_now_add=True)
    log_instance_id = models.CharField(max_length=50)
    log_action_description = models.CharField(max_length=20)
    log_config = models.ForeignKey(Configuration, on_delete=models.CASCADE)
    log_comment = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return str(self.log_instance_id)+"|"+str(self.log_action_description)+"|"+str(self.log_action_date)+"|"+str(self.log_config_id)+"|"+str(self.log_comment)


