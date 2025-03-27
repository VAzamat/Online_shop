from django import forms

from dealer.models import Product, Category


class ProductForm(forms.ModelForm):
    # Наследуемся от специального класса форм, который предоставляет
    # весь необходимый функционал, который нужно настроить
    class Meta:
        model = Product  # Обязательно указываем модель
        exclude = ('views_count','slug')  # и перечисляем поля для отображения

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # Обязательно указываем модель
        fields = '__all__'
