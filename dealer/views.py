from itertools import product

from django.forms.models import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from dealer.models import Product, Category, Version
from dealer.forms import ProductForm, CategoryForm, VersionForm

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
    form_class = ProductForm
    success_url = reverse_lazy('dealer:list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    def get_success_url(self):
        return reverse('dealer:detail', args=[self.kwargs.get('pk')] )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            new_item = form.save()
            new_item.slug = slugify(new_item.product_name)
            new_item.save()

            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dealer:list')


    def form_valid(self, form):
        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.product_name)
            new_item.save()
        return super().form_valid(form)
