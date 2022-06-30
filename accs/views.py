from django.http import request
from accs.models import Quiz
from django.shortcuts import redirect, render
from .models import *
from .forms import QuizForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(req):
    return render(req, 'accs/dashboard.html')

def register(req):
    f = UserCreationForm()

    if req.method == "POST":
        f = UserCreationForm(req.POST)
        if f.is_valid():
            f.save()
            return redirect('/accounts/login/')
    
    ctx = {'form':f}

    return render(req, 'registration/register.html', ctx)

@login_required
def quizs(req):

    quizs = Quiz.objects.all()

    ctx = {'quizs':quizs}

    return render(req, 'accs/quizs.html', ctx)

@login_required
def createQuiz(req):
    questions = Question.objects.all()

    if req.method == 'POST':

        if req.POST.get("del", "") == "false":

            keys = req.POST.keys()
            values = []
            for k in keys:
                values.append(req.POST.get(k, ""))

            datad = dict(zip(keys,values))

            proc_data(datad, req)

        else:
            pid = req.POST.get("id", "")
            delQuiz = Quiz.objects.get(id=pid)
            delQuiz.delete()
        return redirect('/quizs/')

    ctx = {'questions':questions}

    return render(req, 'accs/quizForm.html', ctx)
    
# @login_required
# def updateQuiz(req, pk):

#     upd_quiz = Quiz.objects.get(id=pk)

#     form = QuizForm(instance=upd_quiz)

#     if req.method == 'POST':
#         form = QuizForm(req.POST, instance=upd_quiz)
#         if form.is_valid():
#             form.save()
#             return redirect('/quizs/')

#     ctx = {'form':form}

#     return render(req, 'accs/quizForm.html', ctx)

@login_required
def results(req, pk):

    q = Quiz.objects.get(id=pk)

    datai = q.res

    data = list(map(int, datai[1:-1][1:-1].split("', '")))

    datao = []

    t = 0
    c = 0

    for i in range(5):
        for j in range(c, c+4):
            t += data[j]
        datao.append(t)
        c += 4
        t = 0

    ctx = {'data':datao}

    return render(req, 'accs/res.html', context=ctx)

@login_required
def deleteQuiz(req, pk):

    upd_quiz = Quiz.objects.get(id=pk)

    if req.method == 'POST':
        upd_quiz.delete()
        return redirect('/quizs/')

    ctx = {'item':upd_quiz}

    return render(req, 'accs/delete.html', context=ctx)

def proc_data(datad, req):

    datad.pop('csrfmiddlewaretoken')
    datad.pop('del')

    ans = []

    for k,v in datad.items():
        # Question.objects.filter(id=k).update(val=v)
        q = Question.objects.get(pk=k)
        q.val = v
        q.save()
        ans.append(v)

    qz = Quiz(uname=req.user, res=ans)
    qz.save()