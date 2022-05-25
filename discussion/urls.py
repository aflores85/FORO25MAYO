from django.db import router
from rest_framework import routers
from discussion.views import discussionViewSet

router = routers.DefaultRouter()
router.register(r"discussion", discussionViewSet, "discussion") #quien es el encargado de responder la ruta
