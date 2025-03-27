from django import forms

from dealer.models import Product, Category, Version

forbidden_words = ["бесплатно", "биржа", "биржам", "биржами", "биржах", "бирже", "биржей", "биржи", "биржу", "дешево", "дешевле", "казино", "крипта", "криптам", "криптами", "криптах", "крипте", "криптовалют", "криптовалюта", "криптовалютам", "криптовалютами", "криптовалютах", "криптовалюте", "криптовалютой", "криптовалюту", "криптовалюты", "криптой", "крипту", "крипты", "обман", "обмана", "обманам", "обманами", "обманах", "обмане", "обманов", "обманом", "обману", "обманы", "полицией", "полиции", "полиций", "полицию", "полиция", "полициям", "полициями", "полициях", "радар", "радара", "радарам", "радарами", "радарах", "радаре", "радаров", "радаром", "радару", "радары"]

class ProductForm(forms.ModelForm):
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

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # Обязательно указываем модель
        fields = '__all__'

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version  # Обязательно указываем модель
        fields = '__all__'