Для запуска проекта необходима установка Docker.
Для разворачивания контейнеров следует выполнить следующие команды.

## Запуск Airflow
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.5/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up
```

## Запуск Postgres
```bash
docker run --name postgres_database -d -p 5436:5432 -e POSTGRES_PASSWORD=yandex postgres:alpine
```

