# Проект онлайн-магазина, который демонстрирует категории и входящие в них товары.

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

Ключевые слова:
- 20.1 Работа с ORM в Django
- Урок 20.1
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
python manage.py runserve
```


### Критерии выполнения заданий
- [x] В приложении созданы модели: Product, Сategory.
- [x] Введены для каждой модели требуемые поля
- [x] Сделана связь продукта и категории, используя связь между таблицами «Один ко многим».
- [x] Сформированы фикстуры для заполнения базы данных
- [x] Написана кастомная команда, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от старых данных


#### подробнее
В приложении созданы модели:

- Product, 
- Сategory.

Для каждой модели введены следующие поля:

 - Product 
   - Наименование 
   - Описание
   - Изображение (превью)
   - Категория
   - Цена за покупку
   - Дата создания (записи в БД)
   - Дата последнего изменения (записи в БД)
   
 - Category
   - Наименование
   - Описание

Сделана связь продукта и категории, используя связь между таблицами «Один ко многим».

Сформированы фикстуры для заполнения базы данных.

Написана кастомная команда, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от старых данных.
