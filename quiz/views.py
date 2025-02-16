from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
import random


# Create your views here.

def home_page(request):
    question = Question.objects.all().first()
    return render(request, 'quiz/home_page.html', {
        'question': question
    })

def question_list(request, pk):
    questions = get_object_or_404(Question, pk=pk)
    options = [questions.correct_answer] + questions.incorrect_answers
    category = questions.question_category
    if request.method == "POST":
        return render(request, 'quiz/question_list.html', {
        'questions': questions,
        'options': options,
        'category': category,
    })
    else:
        return render(request, 'quiz/question_list.html', {
        'questions': questions,
        'options': options,
        'category': category,
    })
    
