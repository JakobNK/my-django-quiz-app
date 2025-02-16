from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('quiz/start/<int:pk>', views.question_list, name='question_list')
]