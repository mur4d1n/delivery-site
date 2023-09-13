from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from market.views.category import CategoryViewSet
from market.views.index import index


router = routers.DefaultRouter()
router.register('category', CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Delivery API",
        default_version='v1',
        description="""
                Documentation `ReDoc` view can be found [here](/doc)
        """,
        terms_of_service="https://google.com/policies/terms",
        contact=openapi.Contact(email="mur4d1n@yandex.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', index),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('generic/', include(router.urls)),
        path('market/', include('market.urls'))
    ]))
]
