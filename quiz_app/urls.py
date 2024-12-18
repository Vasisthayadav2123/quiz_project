from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/<int:session_id>/', views.quiz_question, name='quiz_question'),
    path('submit_answer/<int:session_id>/', views.submit_answer, name='submit_answer'),
    path('results/<int:session_id>/', views.quiz_results, name='quiz_results'),
]
