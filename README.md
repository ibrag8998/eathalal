# Ешь Халяль

## Запуск

### Локально

Для удобства, настраиваем окружение и запускаем без докера:

```shell
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt

python app.py
```

### Продакшн

Тут уже удобнее с докером:

```shell
docker-compose up --build
```
