# Ешь Халяль

## Запуск

Перед запуском необходимо создать файл `.env` в корне проекта 
и задать переменную окружения `BOT_TOKEN`:

```dotenv
BOT_TOKEN=123123123:asdasfdsfsdfsdfdsfdsfsdfsdfsdfsdfdsfds
```

### Локально

Для удобства, настраиваем окружение и запускаем без докера:

```shell
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt

python app.py
```

### Продакшн

Деплой на хероку:

```shell
heroku container:push worker
heroku container:release worker
```
