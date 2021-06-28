from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Product, Seller, Category


class CategorySerializer(serializers.ModelSerializer):
    random_photo = SerializerMethodField()

    def get_random_photo(self, obj):
        try:
            return obj.products.first().photo
        except:
            return ''

    class Meta:
        model = Category
        fields = ['id', 'name', 'random_photo']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductsAllInfoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()

    class Meta:
        model = Product
        fields = '__all__'
