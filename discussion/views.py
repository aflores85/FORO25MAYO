from rest_framework import viewsets
from discussion.models import discussion
from discussion.models import discussionSerializer

class discussionViewSet(viewsets.ModelViewSet):
    queryset = discussion.objects.all().order_by("Name_discussion")
    serializer_class = discussionSerializer

