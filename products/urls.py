from django.urls import path, include
from .views import CategoryViewSet, ProductList, ProductListAPIView, SellerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('categories', CategoryViewSet)

router.register('sellers', SellerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products', ProductList.as_view()),
    path('products-filter/', ProductListAPIView.as_view())
]
