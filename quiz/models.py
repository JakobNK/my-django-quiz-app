from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_category = models.CharField(max_length=100)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.JSONField()  # Store incorrect answers as a JSON array
        
    def __str__(self):
        return self.question_text
    
class Scoreboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userName = models.CharField(max_length=100, null=True)
    score = models.BigIntegerField(default=0)
    question_category = models.CharField(max_length=100, blank=True, null=True)
    score_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.score_date = timezone.now()
        self.save()
    
    def __str__(self):
        if self.userName==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.userName