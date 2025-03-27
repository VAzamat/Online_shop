from itertools import product

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from dealer.models import Product, Category

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price')
    success_url = reverse_lazy('dealer:list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price', 'is_active')
    def get_success_url(self):
        return reverse('dealer:detail', args=[self.kwargs.get('pk')] )


    def form_valid(self, form):
        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.product_name)
            new_item.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dealer:list')


    def form_valid(self, form):
        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.product_name)
            new_item.save()
        return super().form_valid(form)
