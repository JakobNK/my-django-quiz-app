from django.shortcuts import render, get_object_or_404
from .models import Question
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect


# Create your views here.

def question_list(request):
    return render(request, 'quiz/question_list.html', {
        
    })