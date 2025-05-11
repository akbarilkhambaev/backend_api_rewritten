from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', CategoryViewSet, basename='subcategory')
router.register('services', CategoryViewSet, basename='service')
router.register('news', CategoryViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)