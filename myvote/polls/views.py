from rest_framework import generics

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer
# Create your views here.
from django.http import HttpResponse


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class VoteView(generics.UpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = VoteSerializer
