from rest_framework import viewsets
from subject.models import subject
from subject.models import subjectSerializer

class subjectViewSet(viewsets.ModelViewSet):
    queryset = subject.objects.all().order_by("Name_subject")
    serializer_class = subjectSerializer
 
