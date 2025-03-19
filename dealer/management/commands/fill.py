from unicodedata import category

from django.core.management import BaseCommand
from dealer.models import Category, Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        запуск отдельной функции
        """
        self.clear_databases()
        self.handle_bulk_create(*args, **options)

    def clear_databases(self):
        Product.objects.all().delete()
        Category.objects.all().delete()

    def handle_bulk_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """
        category_list = [
            {'category_name': 'Пицца', 'description': 'Круглые двух размеров на слоенном тесте'},
            {'category_name': 'Закуски', 'description': 'Простенькие в изготовлении для утоления  голода'},
            {'category_name': 'Напитки', 'description': 'Жидкости для питья'},
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'product_name': 'Пеперони', 'description': 'Круглая пицца с колбасой и зеленью', 'category': Category.objects.get(category_name='Пицца'),  'price':100.},
            {'product_name': 'Маргарита', 'description': 'Круглая пицца с помидорами и сыром', 'category': Category.objects.get(category_name='Пицца'), 'price':200.},
            {'product_name': 'Вишневый компот', 'description': 'Стакан с напитком. 100% вишневый сок. Охлажденный', 'category': Category.objects.get(category_name='Напитки'), 'price':20.0},
        ]
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))
        Product.objects.bulk_create(product_for_create)



