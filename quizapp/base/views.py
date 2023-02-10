from django.shortcuts import render,redirect
from .models import Player,Question,Quiz
import requests
import random
import numpy as np
# Create your views here.

def createPlayer(request):
    quizs = Quiz.objects.all()[:5]

    context = {"quizs":quizs}
    if request.method == "POST":
        name = request.POST.get('name')
        player = Player.objects.create(name = name)
        player.save()
        quiz = Quiz.objects.create(player = player)
        quiz.save()
        x = requests.get("https://the-trivia-api.com/api/questions")
        print(x.json())
        number = 1
        for object in x.json():
            array = object["incorrectAnswers"].copy()
            array.append(object["correctAnswer"])
            random.shuffle(array)
            q = Question.objects.create(
                number = number, 
                category = object["category"],
                difficulty = object["difficulty"],
                question = object["question"],
                correctAnswer = object["correctAnswer"],
                incorrect = object["incorrectAnswers"],
                choices = array,
                quiz = quiz,
            )
            q.save()
            number+=1
        return redirect("quiz",pk = quiz.id)
    return render(request,"base/home.html",context)

def quizView(request,pk):
    quiz = Quiz.objects.get(id = pk)
    questions = Question.objects.filter(quiz = quiz)
    print(questions)
    if quiz.completed == True:
        return redirect("result",pk = quiz.id)
    if request.method == "POST":
        for obj in questions:
            print("---")
            for x in obj.choices:
                test = request.POST.get(x)
                if test is not None:
                    obj.playerChoice = x
                    obj.save()
                    print(obj.playerChoice)
                    if obj.playerChoice == obj.correctAnswer:
                        quiz.correctQuestions +=1
                        break
                    else:
                        break
        print(quiz.correctQuestions)
        quiz.completed = True
        quiz.save()
        return redirect("result",pk = quiz.id)          
    context = {"questions": questions}
    return render(request,"base/quiz.html",context)

def resultView(request,pk):
    quiz = Quiz.objects.get(id = pk)
    questions = Question.objects.filter(quiz = quiz)
    print(questions)
    context = {"questions" : questions,"quiz":quiz}
    return render(request,"base/result.html",context)