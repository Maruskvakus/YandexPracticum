Для запуска проекта необходима установка Docker.
Для разворачивания контейнеров следует выполнить следующие команды.

#Запуск Airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.5/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up

#Запуск Postgres
docker run -d --name postgres postgres:alpine -e POSTGRES_PASSWORD=yandex -p 5436:5436
