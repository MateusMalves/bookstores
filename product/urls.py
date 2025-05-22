from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path("", include(router.urls)),
]