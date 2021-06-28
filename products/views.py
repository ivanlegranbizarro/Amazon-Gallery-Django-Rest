from re import search
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Product, Category, Seller
from .serializers import (
    ProductsAllInfoSerializer,
    ProductsSerializer,
    SellerSerializer,
    CategorySerializer
)

# Create your views here.


class ProductList(APIView):
    """
    List all products or create new one
    """

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsAllInfoSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    filter_fields = (
        'category__id',
    )
    search_fields = (
        'title',
    )


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
