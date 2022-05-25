from rest_framework import viewsets
from questions.models import questions
from questions.models import questionsSerializer

class questionsViewSet(viewsets.ModelViewSet):
    queryset = questions.objects.all().order_by("Name_questions")
    serializer_class = questionsSerializer

