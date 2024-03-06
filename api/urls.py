from django.urls import include, path 

from rest_framework.routers import DefaultRouter

from api.views import BookViewSet, CategoryViewSet

router_v1 = DefaultRouter()

router_v1.register(r'books', BookViewSet, basename='book')
router_v1.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]