from django.template.defaulttags import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from api_quiz.views import QuizModelViewSet

app_name = "api_quiz"
# Создаём Router и регистрируем ViewSet
router = DefaultRouter()
router.register(r"quizzes", QuizModelViewSet)

urlpatterns = []
urlpatterns += router.urls
