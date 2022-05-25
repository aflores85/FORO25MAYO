from rest_framework import viewsets
from Forum.models import forum
from Forum.models import forumSerializer

class ForumViewSet(viewsets.ModelViewSet):
    queryset = forum.objects.all().order_by("Name_forum")
    serializer_class = forumSerializer

