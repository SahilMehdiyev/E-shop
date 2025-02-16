from rest_framework import generics
from product import models as product_models
from .serializers import ProductSerializer

class ProductAPIView(generics.ListAPIView):
    queryset = product_models.Product.objects.all()
    serializer_class = ProductSerializer
    