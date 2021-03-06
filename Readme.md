Инструкция по запуску
===========
Для запуска проекта необходима установка Docker.
Для разворачивания контейнеров следует выполнить следующие команды.

### Запуск Airflow
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.5/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up
```

### Запуск Postgres
```bash
docker run --name postgres_database -d -p 5436:5432 -e POSTGRES_PASSWORD=yandex postgres:alpine
```

### Клонирование скриптов
Для запуска процесса необходимо скопировать файлы из папки dags в репозитории в папку dags, 
которая создается при установке на локальном компьютере в корневой папке пользователя.

### Запуск процесса
Для запуска ETL процесса необходимо зайти на [сервер airflow](http://localhost:8080) и 
включить выполнение процесса **currency**. Логин и пароль для сервера - ***airflow***.
Там же на сервере возможно отслеживать выполнение процесса. 
Дополнительные настройки, например, отправку уведомлений можно настроить в файле сurrency_dag.py.

