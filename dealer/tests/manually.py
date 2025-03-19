
from dealer.models import  Category, Product
category_item = {'category_name': 'Супы', 'description': 'Жидкие холодные или горячие блюда (борщи,солянки,харчо и т.п.)'}
category_ = Category.objects.create(**category_item)
cat1 = Category.objects.get(category_name="Супы")
product_item = {'product_name': 'Борщ', 'description': 'традиционный капустный суп окрашенный свекольным соком', 'category': cat1, 'price':150.0}
Product.objects.create(**product_item)
product_item = {'product_name': 'Харчо', 'description': 'традиционный слегка острый грузинский суп', 'category': cat1, 'price':120.0}
Product.objects.create(**product_item)
