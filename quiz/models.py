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