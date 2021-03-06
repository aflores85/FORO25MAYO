from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework import routers
from . import settings

from drf_yasg.views import get_schema_view   
from drf_yasg import openapi

from answers.urls import router as answers_Router
from discussion.urls import router as discussion_Router
from Forum.urls import router as forum_Router
from questions.urls import router as questions_Router
from subject.urls import router as subject_Router
#traer todos los router de la aplicacion.


router = routers.DefaultRouter()
router.registry.extend(answers_Router.registry)
router.registry.extend(discussion_Router.registry)
router.registry.extend(forum_Router.registry)
router.registry.extend(questions_Router.registry)
router.registry.extend(subject_Router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="FullStack Django",
        default_version="V1",
        description="Ejemplo de Endpoint con DRF",
        contact=openapi.Contact(email="aflores85@gmail.com")
        
    ),
    public=True
)

static_urlpatterns = [
    re_path(r"^static/(?P<path>.*", serve, {"document_root":settings.STATIC_ROOT})
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
