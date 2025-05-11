from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet, ServiceViewSet, NewsViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('services', ServiceViewSet)
router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
