from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('quizs/', views.quizs, name="quizs"),
    path('results/<str:pk>/', views.results, name="results"),
    path('createQuiz/', views.createQuiz, name="createQuiz"),
    # path('updateQuiz/<str:pk>/', views.updateQuiz, name="updateQuiz"),
    path('deleteQuiz/<str:pk>/', views.deleteQuiz, name="deleteQuiz")
]
