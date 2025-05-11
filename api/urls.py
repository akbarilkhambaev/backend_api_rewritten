from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import CategoryViewSet, SubcategoryViewSet, ServiceViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('categories', CategoryViewSet)
sub_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
sub_router.register('subcategories', SubcategoryViewSet, basename='category-subcategories')

serv_router = routers.NestedDefaultRouter(sub_router, 'subcategories', lookup='subcategory')
serv_router.register('services', ServiceViewSet, basename='subcategory-services')
router.register('news', CategoryViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)