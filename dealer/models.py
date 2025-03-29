from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.pk} {self.category_name}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов

class Product(models.Model):
    product_name = models.CharField(max_length=120, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview_image = models.ImageField(upload_to="preview/", verbose_name="изображение", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='цена')
    created_at = models.DateTimeField(verbose_name='дата создания',default=now, editable=False)
    updated_at = models.DateTimeField(verbose_name='дата изменения',default=now, editable=True)
    views_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Опубликованность"
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="slug",
        help_text="человекочитаемая ссылка"
    )

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} из категории   {self.category} по цене {self.price}'

    class Meta:
        verbose_name = 'продукт' # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты' # Настройка для наименования набора объектов

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_name = models.CharField(max_length=70, verbose_name='Наименование версии')
    version_number = models.CharField(max_length=10, verbose_name='Номер версии')
    is_active = models.BooleanField( default=False,  verbose_name="Активная/Неактивная" )

    def __str__(self):
        if self.is_active:
            return f'[X]{self.version_number} {self.version_name} для {self.product}'
        else:
            return f'[-] {self.version_number} {self.version_name} для {self.product}'

    class Meta:
        verbose_name = 'версия' # Настройка для наименования одного объекта
        verbose_name_plural = 'версии' # Настройка для наименования набора объектов