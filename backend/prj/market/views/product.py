from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Product
from market.views.category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'category']


class ProductListView(ListAPIView, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

