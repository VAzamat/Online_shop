from django.urls import path

from dealer.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from dealer.apps import DealerConfig

app_name = DealerConfig.name

urlpatterns = [
    #path("", index, name='index'),
    path("",                  ProductListView.as_view(), name='list'),
    path("Product/<int:pk>/", ProductDetailView.as_view(), name='detail'),
    path("Product/create/",   ProductCreateView.as_view(), name='create'),
    path("Product/update/<int:pk>/", ProductUpdateView.as_view(), name='update'),
    path("Product/delete/<int:pk>/", ProductDeleteView.as_view(), name='delete'),
]
