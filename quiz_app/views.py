import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, QuizSession

def start_quiz(request):
    # Start a new quiz session
    quiz_session = QuizSession.objects.create(user="User1")
    return redirect('quiz:quiz_question', session_id=quiz_session.id)

def quiz_question(request, session_id):
    # Fetch a random question
    quiz_session = QuizSession.objects.get(id=session_id)
    question = random.choice(Question.objects.all())
    return render(request, 'quiz_app/question.html', {'question': question, 'session_id': session_id})

def submit_answer(request, session_id):
    quiz_session = QuizSession.objects.get(id=session_id)
    question_id = request.POST.get('question_id')
    selected_answer = request.POST.get('answer')

    question = Question.objects.get(id=question_id)
    if selected_answer == question.correct_answer:
        quiz_session.correct_answers += 1
    else:
        quiz_session.incorrect_answers += 1
    quiz_session.total_questions += 1
    quiz_session.save()

    # Check if there are more questions or finish
    if quiz_session.total_questions < 5:  # You can set any limit on number of questions
        return redirect('quiz:quiz_question', session_id=session_id)
    else:
        return redirect('quiz:quiz_results', session_id=session_id)

def quiz_results(request, session_id):
    quiz_session = QuizSession.objects.get(id=session_id)
    return render(request, 'quiz_app/results.html', {'quiz_session': quiz_session})
