from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        #fields = "__all__"
        fields = ('correct_answer' + 'incorrect_answers')
        print(fields)