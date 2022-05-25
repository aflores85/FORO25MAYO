from django.db import router
from rest_framework import routers
from Forum.views import ForumViewSet

router = routers.DefaultRouter()
router.register(r"forum", ForumViewSet, "forum") #quien es el encargado de responder la ruta
