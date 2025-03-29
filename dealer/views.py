
from django.forms.models import inlineformset_factory


from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from dealer.models import Product, Category, Version
from dealer.forms import ProductForm, CategoryForm, VersionForm

class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        active_versions = [ "" for i in range(len(context_data['object_list'])) ]
        for num, object in enumerate( context_data['object_list']):
            versions = Version.objects.select_related().filter(product=object.pk)
            for version in versions:
                if version.is_active:
                    active_versions[num] = version.version_number
        context_data['active_versions'] = active_versions
        return context_data
        #        product_id = Product.objects.filter(pk=kwargs['object'].pk)[0]

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_id = Product.objects.filter(pk=kwargs['object'].pk)[0]
        versions = Version.objects.select_related().filter(product=product_id)
        for version in versions:
            if version.is_active:
                context_data['active_version'] = version.version_number
        return context_data

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('dealer:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def is_single_true(self, myforms):
        count_true = 0
        for form_item in myforms:
            if form_item["is_active"].value():
                count_true += 1
        return count_true<2

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.product_name)
            new_item.save()

        if self.is_single_true(formset.forms):
            if formset.is_valid():
                self.object = form.save()
                formset.instance = self.object
                formset.save()
        else:
            form.add_error('product_name', 'Только одна версия может быть активной')
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

        return super().form_valid(form)


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

    def is_single_true(self, myforms):
        count_true = 0
        for form_item in myforms:
            if form_item["is_active"].value():
                count_true += 1
        return count_true<2

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.product_name)
            new_item.save()

        if self.is_single_true(formset.forms):
            if formset.is_valid():
                self.object = form.save()
                formset.instance = self.object
                formset.save()
        else:
            form.add_error('product_name', 'Только одна версия может быть активной')
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

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
