from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.createPlayer,name = "home"),
    path("quiz/<str:pk>",views.quizView,name = "quiz"),
    path("quiz/<str:pk>/result",views.resultView,name = "result")
]