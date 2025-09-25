from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Question

# Create your views here.
def index(request):
    display_question = Question.objects.all()
    return render(request, 'index.html', {'display_question': display_question})

def save_question(request):
    question = Question(question_text=request.POST['question_text'],)

    Question.objects.create(question_text = question, pub_date = datetime.now())
    return redirect('polls:index')