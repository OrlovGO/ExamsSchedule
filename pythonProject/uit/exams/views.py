from django.shortcuts import render
from .models import Exam, Schedule, Subject, Program
# Create your views here.

def index(request):
    exam = Exam.objects.all()
    schedule = Schedule.objects.all()
    subject = Subject.objects.all()
    program = Program.objects.all()

    context = {'exam': exam, 'schedule': schedule, 'subject': subject, 'program': program}

    return render(request, 'exams/Schedule.html', context)
