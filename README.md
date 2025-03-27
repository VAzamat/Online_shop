# Проект онлайн-магазина, который демонстрирует категории и входящие в них товары.
## 22.1 Forms Formsets

Ветки:
  * wip_19.2_django_project_basic_configuration 
    - базовая настройка config/settings.py
    - startapp dealer
    - home.html webpage
  
  * wip_20.1_django_databases_ORM
    - согласно 20.1 Работа с ORM в Django
    - создана база данных и настроена связь с ней
    - созданы модели для Product и Category (см. ниже)
    - настроена админка
    - фикстура (fixture) для сохранения данных в dealer/dumpfile/dump.json и восстановления из него
    - кастомная(консольная) команда fill для заполнения базы данных (dealer/management/commands/fill.py)
  
  * wip_20.2_django_statics_templates
    - согласно 20.2 Шаблонизация в Django
    - Добавлены контроллер и шаблон главной страницы на основе bootstrap:pricing
    - Настроено отображение списка товаров на главной странице в цикле, повторяющиеся части выделены в base.html 
    - Созданы шаблонный фильтр mediapath или шаблонный тег get_media_prefix 

  * wip_CRUD_CBV
    - согласно 21.1 FBV и CBV
    - Реализованы все страницы в CRUD (CreateReadUpdateDelete) парадигме
    - создан счетчик просмотров через функцию self.get_object()
    - перенаправление на динамическую страницу переопределением функции self.get_success_url()
    - выполнение валидации (математического действия) перед сохранением измененного объекта self.form_valid(form) 
    - назначение slug для страниц 
  * wip_Forms_Formsets
    - dd
    - 

Ключевые слова:
- CRUD в Django, Class Based Model - Function Based Model
- счетчик просмотров views_count
- перенаправление на динамическую ссылку
- slug
- Шаблонизация в django
- шаблоны
- templates
- django
- шаблонный фильтр
- шаблонный тег
- Работа с ORM в Django
- django
- postgres
- фикстура (fixture) 
- кастомная (консольная) команда 


### развертывание из клонированного репозитария https://github.com

для работы с database необходимо создать базу данных online_shop_fk9c0r0x_db и пользователю azamat назначить пароль UseVeryStrongPasswordHere (аналогично тем настройкам, что указаны в файле .env)
```sql
#psql (13.4)
#Введите "help", чтобы получить справку.
postgres=# CREATE ROLE azamat LOGIN PASSWORD 'UseVeryStrongPasswordHere';
postgres=# ALTER USER azamat WITH PASSWORD 'UseVeryStrongPasswordHere';
postgres=# DROP DATABASE  IF EXISTS online_shop_fk9c0r0x_db;
postgres=# CREATE DATABASE online_shop_fk9c0r0x_db OWNER azamat;
```

```bash
# клонируем репозиторий
git clone https://github.com/VAzamat/Online_shop/
# переходим в директорию
cd Online_shop/
# создаем виртуальное окружение
 python3 -m venv env #создаем виртуальное окружение
# активируем виртуальное окружение
 source env/bin/activate #переходим в виртуальное окружение
# редактируем .env (можно скопировать из минимально рабочую конфигурацию из .env.example)
mv .env.example .env
# активируем настройки переменных окружения из текущей директории
source .env
# Устанавливаем зависимости
pip3 install -r requirements.txt
# создание миграций
python manage.py makemigrations
# применение миграций
python manage.py migrate
 
#Для создания суперпользователя используется  команда
python manage.py createsuperuser
#заполнение базы данных через кастомную команду dealer/management/commands/fill.py
python manage.py fill
#запускаем сервер и смотрим результат http://127.0.0.1:8000/
python manage.py runserver
```




### Критерии выполнения заданий
- [x] Переведены на Class Based Views
- [x] Динамический slug 
- [x] Сделан счетчик просмотров
- [x] Перенаправление на динамический адрес

### Задание 1

- Переведите имеющиеся контроллеры с FBV на CBV.
> Выполнено 

### Задание 2
Задайте slug - человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или предложения в адресной строке

> Выполнено

### Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

- При открытии отдельной статьи увеличивать счетчик просмотров.
- При создании динамически формировать slug name для заголовка.
- После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.

> Выполнено