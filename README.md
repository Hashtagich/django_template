# Шаблон для Django проектов

<details>

<summary>

## Уточнения по структуре

</summary>

#### 1. При создании нового приложения в проекте необходимо добавить его в список *INSTALLED_APPS* в файле 
```backend/backend/setting.py```
#### 2. Если хочется чтобы в админ-панеле название приложения было на русском языке, то необходимо в файл ```apps.py``` данного приложения добавить в класс следующий атрибут *verbose_name = "Название приложения"*
#### 3. Все представления и сериализаторы пишутся в приложении *api* в директориях ```api/v1/serializers``` и ```api/v1/serializers``` соответсвенно, названия лучше писать так *nameapp_views* т.е. название приложения_views
#### 4. Центральный urls находится в корне приложения *api*. В случаи перехода на версию api №2, например ```v2```, то достаточно создать пакет v2 с сериализаторами, представления и urls и добавить ```path('api/v2/', include('api.v2.urls')),``` в список *urlpatterns* в центральный urls.
#### 5. Пакет *v1* и разделение вообще на версии создан для плавного перехода между версиями приложения
#### 6. Модели и отображение в админ-панели т.е. файлы ```models.py``` и ```admin.py``` создаются в каждом приложении персонально.
#### 7. Файл ```.env``` расположен в корне проекта для его использования в docker compose и сторонних сервисах, чтобы не плодить кучу env файлов в каждом сервисе.

</details>

___

## Запуск проекта

___

<details>

<summary>

### Первый способ, через Docker compose

</summary>

### 1. Создаём новый репозиторий на основе данного репозитория


### 2. Установка переменных окружения

***В корен проекта заполняем файл .env.template и переименовываем его в .env или просто создаём файл .env и
заполняем его***

 ```bash
 BACKEND_SERVER__SECRET_KEY='Ваш секретный ключ проекта'
 BACKEND_SERVER__DEBUG=Булевое значение True или False
 BACKEND_SERVER__DJANGO_ALLOWED_HOSTS='Разрешенные хосты'
 BACKEND_SERVER__CSRF_TRUSTED_ORIGINS='Разрешенные источники'
 BACKEND_SERVER__LANGUAGE_CODE='Язык, например, ru'
 BACKEND_SERVER__TIME_ZONE='Временная зона, например, UTC'
 BACKEND_SERVER__PORT_HOST=Порт внешний, например, 8000
 BACKEND_SERVER__PORT_CONTAINER=Порт внутренний, например, 8000

 DB__NAME='Имя Базы данных (БД), например, db'
 DB__LOGIN='Логин БД, например, db'
 DB__PASS='Пароль БД, например, db'
 DB__HOST='Хост БД, например, db'
 DB__PORT_HOST='Порт БД внешний, например, 5433'
 DB__PORT_CONTAINER='Порт БД внутренний, например, 5432'
 
 EMAIL__BACKEND='Сервис для почты, например, django.core.mail.backends.smtp.EmailBackend'
 EMAIL__HOST='Хост почты, например для gmail smtp.gmail.com или smtp.mail.ru для mail'
 EMAIL__PORT=Порт почты, например, 587
 EMAIL__DEFAULT='Почта с которой будет отправлять письма youremail@gmail.com если выбрали smtp.gmail.com'
 EMAIL__USE_TLS=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
 EMAIL__USE_SSL=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
 EMAIL__HOST_PASSWORD='Пароль для внешнего приложения для доступа к почте, подробнее тут https://help.mail.ru/mail/security/protection/external/'
 EMAIL__NOTIFICATION='Перечень почт куда будут отправлять письма, пишите через пробел, можно указать одну'

 CELERY__BROKER_URL='URL-адрес брокера сообщений, например,redis://localhost:6379'
 CELERY__RESULT_BACKEND='Место хранения результатов выполнения задач, например,redis://localhost:6379'
 CELERY__ACCEPT_CONTENT='Список форматов, которые Celery будет принимать в качестве контента для задач, например,application/json'
 CELERY__TASK_SERIALIZER='Сериализатор, который будет использоваться для сериализации задач перед их отправкой, например,json'
 CELERY__RESULT_SERIALIZER='Сериализатор, который будет использоваться для сериализации результатов задач, например,json'
 
 NGINX__PORT_HOST='Порт NGINX внешний, например, 80'
 NGINX__PORT_CONTAINER='Порт NGINX внутренний, например, 80'
 ```

### 3. Сборка и запуск контейнеров

```bash
docker-compose up --build -d
```

### 4. Создание суперпользователя (при необходимости)

```bash
docker-compose exec web python manage.py createsuperuser
```

</details>

<details>

<summary>

### Второй способ, без использования Docker compose

</summary>

### 1. Создаём новый репозиторий на основе данного репозитория

2. Запускаем backend

   2.1. Установите и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    venv/Scripts/activate  - для Windows
    venv/bin/activate - для Linux
    ```

   2.2 Установка переменных окружения:
   ***В корен проекта заполняем файл .env.template и переименовываем его в .env или просто создаём файл .env и
   заполняем его***

       ```bash
       BACKEND_SERVER__SECRET_KEY='Ваш секретный ключ проекта'
       BACKEND_SERVER__DEBUG=Булевое значение True или False
       BACKEND_SERVER__DJANGO_ALLOWED_HOSTS='Разрешенные хосты'
       BACKEND_SERVER__CSRF_TRUSTED_ORIGINS='Разрешенные источники'
       BACKEND_SERVER__LANGUAGE_CODE='Язык, например, ru'
       BACKEND_SERVER__TIME_ZONE='Временная зона, например, UTC'
       BACKEND_SERVER__PORT_HOST=Порт внешний, например, 8000
       BACKEND_SERVER__PORT_CONTAINER=Порт внутренний, например, 8000
      
       DB__NAME='Имя Базы данных (БД), например, db'
       DB__LOGIN='Логин БД, например, db'
       DB__PASS='Пароль БД, например, db'
       DB__HOST='Хост БД, например, db'
       DB__PORT_HOST='Порт БД внешний, например, 5433'
       DB__PORT_CONTAINER='Порт БД внутренний, например, 5432'
       
       EMAIL__BACKEND='Сервис для почты, например, django.core.mail.backends.smtp.EmailBackend'
       EMAIL__HOST='Хост почты, например для gmail smtp.gmail.com или smtp.mail.ru для mail'
       EMAIL__PORT=Порт почты, например, 587
       EMAIL__DEFAULT='Почта с которой будет отправлять письма youremail@gmail.com если выбрали smtp.gmail.com'
       EMAIL__USE_TLS=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
       EMAIL__USE_SSL=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
       EMAIL__HOST_PASSWORD='Пароль для внешнего приложения для доступа к почте, подробнее тут https://help.mail.ru/mail/security/protection/external/'
       EMAIL__NOTIFICATION='Перечень почт куда будут отправлять письма, пишите через пробел, можно указать одну'
      
       CELERY__BROKER_URL='URL-адрес брокера сообщений, например,redis://localhost:6379'
       CELERY__RESULT_BACKEND='Место хранения результатов выполнения задач, например,redis://localhost:6379'
       CELERY__ACCEPT_CONTENT='Список форматов, которые Celery будет принимать в качестве контента для задач, например,application/json'
       CELERY__TASK_SERIALIZER='Сериализатор, который будет использоваться для сериализации задач перед их отправкой, например,json'
       CELERY__RESULT_SERIALIZER='Сериализатор, который будет использоваться для сериализации результатов задач, например,json'
       
       NGINX__PORT_HOST='Порт NGINX внешний, например, 80'
       NGINX__PORT_CONTAINER='Порт NGINX внутренний, например, 80'
       ```

   2.3 Перейдите в папку backend и установите зависимости:
    ```bash
    cd backend
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

   2.4 В файле backend/backend/settings.py находим переменную DATABASES и заменяем на:
    ```bash
    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     },
    ```

   2.5 Находясь в папке backend выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

   2.6 Находясь в папке backend создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

   2.7 Находясь в папке backend запустите проект:
    ```bash
    python manage.py runserver
    ```

</details>

___

### API

***URL***

http://127.0.0.1:8000 или http://localhost:8000

***Страница Админ панели***

<code>{{URL}}/admin/</code>

***Страница с документацией по API***

<code>{{URL}}/api/v1/docs/</code>