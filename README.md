# TaskManagerProject

Небольшой HTTP API на FastAPI.

## Запуск в Docker

```bash
docker compose up --build -d
```

API доступен по адресу `http://localhost:8080`, документация —
`http://localhost:8080/docs`. Внутри контейнера Uvicorn слушает порт `1489`.

## Локальный запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 1489
```

## Маршруты

- `GET /` — состояние сервиса.
- `GET /hello/{name}` — приветствие.
- `POST /message` — принимает JSON-объект и возвращает его в поле `received`.

```bash
curl -X POST http://localhost:8080/message \
  -H 'Content-Type: application/json' \
  -d '{"text":"Hello!"}'
```
