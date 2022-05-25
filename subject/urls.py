from django.db import router
from rest_framework import routers
from subject.views import subjectViewSet

router = routers.DefaultRouter()
router.register(r"subject", subjectViewSet, "subject") #quien es el encargado de responder la ruta
