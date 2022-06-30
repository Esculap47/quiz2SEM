from django.contrib.auth.models import User
from .models import Quiz
from django import forms

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'