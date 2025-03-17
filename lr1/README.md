# Лабораторная работа 1 

*k8s*

## Инструкция по запуску в docker compose

1. создать .env файл в корне lr1
2. `docker compose up --build -d`
3. Вручную исполнить следующий скрипт на базе данных:
    ```sql
    create database orders_db;
    create database users_db;
    create database products_db;
    ```
4. поменять в .env файле значение `POSTGRES_HOST` на localhost (особенности работы с 
   сетями внутри docker stack'a)
5. Зайти в каждый сервис и произвести этот скрипт, если установлен uv
    ```shell
    uv run --with alembic --with dotenv --with sqlmodel --with psycopg2-binary alembic upgrade head
   ```
   Или любым другим способом применить миграции на бд

