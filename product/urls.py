from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.ProductAPIView.as_view()),
    path('product/<int:id>/',views.ProductDetailAPIView.as_view()),
]
