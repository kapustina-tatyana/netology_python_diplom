# Дипломная работа к профессии Python-разработчик «API Сервис заказа товаров для розничных сетей».

## Описание

Приложение предназначено для автоматизации закупок в розничной сети. Пользователи сервиса — покупатель (менеджер торговой сети, который закупает товары для продажи в магазине) и поставщик товаров.

**Клиент (покупатель):**

- Менеджер закупок через API делает ежедневные закупки по каталогу, в котором
  представлены товары от нескольких поставщиков.
- В одном заказе можно указать товары от разных поставщиков — это
  повлияет на стоимость доставки.
- Пользователь может авторизироваться, регистрироваться и восстанавливать пароль через API.
    
**Поставщик (магазин):**

- Через API информирует сервис об обновлении прайса.
- Может включать и отключать прием заказов.
- Может получать список оформленных заказов (с товарами из его прайса).


### Задача

Необходимо разработать backend-часть (Django) сервиса заказа товаров для розничных сетей.

**Базовая часть:**
* Разработка сервиса под готовую спецификацию (API);
* Возможность добавления настраиваемых полей (характеристик) товаров;
* Импорт товаров;
* Отправка накладной на email администратора (для исполнения заказа);
* Отправка заказа на email клиента (подтверждение приема заказа).



### Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать базу:

```bash
docker run -d --name postgre5437 -p 5437:5432 -e POSTGRES_USER=diplom_user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=diplom_db postgres
```

Создать файл переменных окружения из примера и заполнить его:

```bash
cp api_shops/dot.env_example api_shops/.env
```

Применить миграции:

```bash
manage.py makemigrations
manage.py migrate
manage.py createsuperuser
```

В разных терминалах выполнить команды:

```bash
python manage.py runserver 0.0.0.0:8037

python -m celery -A api_shops worker -l info
```

Для тестирования можно открыть файл [api_shops.http](api_shops.http)
в VSсode с плагином REST client, указать валидные email и выполнить запросы по списку.


Для удобства отладки, первые два запроса (POST {{baseUrl}}/user/register) возвращают "confirm_token",
его надо прописать в соответствующие переменные, для покупателя и магазина.

Страничка swagger:

![img.png](img.png)

Сработал DRF throttling:

![img_1.png](img_1.png)