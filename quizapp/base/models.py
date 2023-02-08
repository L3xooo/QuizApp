from django.db import models

# Create your models here

class Player(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    correctQuestions = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.player.name + "'s test"

class Question(models.Model):
    number = models.IntegerField(default=0)
    quiz = models.ForeignKey("Quiz",on_delete=models.CASCADE,null = True)
    question = models.CharField(max_length=300)
    correctAnswer = models.CharField(max_length=300)
    category = models.CharField(max_length=300,default = "string")
    incorrect = models.JSONField(default = "")
    difficulty = models.CharField(max_length=20,default = "easy")
    choices = models.JSONField(default= "")
    playerChoice = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.question[:40]
