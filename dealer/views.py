from itertools import product

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from dealer.models import Product, Category

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price')
    success_url = reverse_lazy('dealer:list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price')
    success_url = reverse_lazy('dealer:list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dealer:list')