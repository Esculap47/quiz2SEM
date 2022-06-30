from django.contrib.auth.models import User
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accs.models import Quiz
from api_quiz.serializers import QuizSerializer


class QuizModelViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name',]
    filterset_fields = ['uname',]

    @action(methods=['GET'], detail=False)
    def current_admin_and_not_staff(self, request, *args, **kwargs):
        if self.request.user:
            not_staff_users = User.objects.exclude(is_staff=True)
            qs = self.get_queryset().filter(Q(uname=self.request.user) | Q(uname__in=not_staff_users))
            # print(1/0)
            serializer = QuizSerializer(qs, many=True)
            return Response(serializer.data)
        else:
            return Response({})
