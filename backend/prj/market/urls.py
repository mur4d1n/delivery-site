from django.urls import path, include
from .views.auth import AuthView
from .views.product import ProductListView


urlpatterns = [
    path('user-login/', AuthView.as_view()),
    path('product-list/', ProductListView.as_view())
]