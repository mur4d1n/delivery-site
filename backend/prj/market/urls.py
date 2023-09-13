from django.urls import path, include
from .views.auth import AuthView


urlpatterns = [
    path('user-login/', AuthView.as_view())
]