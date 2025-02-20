from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .models import Question, Scoreboard
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse, JsonResponse
import random
from datetime import timedelta

# Create your views here.


def home_page(request):
    today = timezone.now().date()
    question = Question.objects.filter(created_date__date=today).first()
    scoreboard = Scoreboard.objects.all()
    #scoreboard_date = Scoreboard.objects.filter(user=request.user).first().score_date.date()
    today = timezone.now().date()
    return render(request, 'quiz/home_page.html', {
        'question': question,
        'scoreboard': scoreboard,
        'lockout': False
        })   

    
def scoreboard(request):
    scoreboard = Scoreboard.objects.all()
    return render(request, 'quiz/scoreboard.html', {
        'scoreboard': scoreboard
    })

def question_list(request, pk):
    today = timezone.now().date()
    questions = get_object_or_404(Question.objects.filter(created_date__date=today), pk=pk)
    print(questions)
    options = [questions.correct_answer] + questions.incorrect_answers
    random.shuffle(options) #Shuffle options so the correct is not always first
    category = questions.question_category
    scoreboard = Scoreboard.objects.filter(user=request.user).first()
    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        if selected_answer == questions.correct_answer:
            scoreboard.score = scoreboard.score + 1
            scoreboard.save()
            
        next_question = Question.objects.filter(id__gt=questions.pk).order_by('id').first()
        if next_question:
            return redirect('question_list', pk = (questions.pk+1))  # Redirect to next question
        else:
            scoreboard.score_date = timezone.now()
            scoreboard.save()
            return redirect('scoreboard')  # Redirect to results or a completion page

    else:
        if scoreboard.score_date.date() == today:
            lockout = True
        else:
            lockout = False
            
        return render(request, 'quiz/question_list.html', {
            'questions': questions,
            'options': options,
            'category': category,
            'lockout': lockout
        })
        
    
def sign_up(request):
    form_class = UserCreationForm(request.POST or None)
    succes_url = reverse_lazy("home_page")
    if request.method == 'POST' and form_class.is_valid():
        #We need logic here to create a user in the database
        #form_class.save() 
        user = form_class.save()

        Scoreboard.objects.create(
            user=user,  # Assign the newly created user
            userName=user,  # Optional: Store the username
            score_date=timezone.now()-timedelta(1)
        )
        
        login(request, user)
        
        return redirect(succes_url)
    else:
        #Render the signup page so people can create a new account
        return render(request, 'registration/signup.html', {
            'form': form_class
        })