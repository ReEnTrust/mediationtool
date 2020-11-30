import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField('date published')
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=20)
    body=models.CharField(max_length=500)

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
