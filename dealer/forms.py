from django import forms
from django.forms import BooleanField

from dealer.models import Product, Category, Version

forbidden_words = ["бесплатно", "биржа", "биржам", "биржами", "биржах", "бирже", "биржей", "биржи", "биржу", "дешево", "дешевле", "казино", "крипта", "криптам", "криптами", "криптах", "крипте", "криптовалют", "криптовалюта", "криптовалютам", "криптовалютами", "криптовалютах", "криптовалюте", "криптовалютой", "криптовалюту", "криптовалюты", "криптой", "крипту", "крипты", "обман", "обмана", "обманам", "обманами", "обманах", "обмане", "обманов", "обманом", "обману", "обманы", "полицией", "полиции", "полиций", "полицию", "полиция", "полициям", "полициями", "полициях", "радар", "радара", "радарам", "радарами", "радарах", "радаре", "радаров", "радаром", "радару", "радары"]

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control text-start'

class ProductForm(StyleFormMixin, forms.ModelForm):
    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        for word in forbidden_words:
            if  word in cleaned_data:
                raise forms.ValidationError('Вы используете запрещенные слова в названии')

        return cleaned_data
    # Наследуемся от специального класса форм, который предоставляет
    # весь необходимый функционал, который нужно настроить
    class Meta:
        model = Product  # Обязательно указываем модель
        exclude = ('views_count','slug')  # и перечисляем поля для отображения

class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category  # Обязательно указываем модель
        fields = '__all__'

class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version  # Обязательно указываем модель
        fields = ('product','version_name','version_number','is_active')
