from django.db import router
from rest_framework import routers
from questions.views import questionsViewSet

router = routers.DefaultRouter()
router.register(r"questions", questionsViewSet, "questions") #quien es el encargado de responder la ruta
