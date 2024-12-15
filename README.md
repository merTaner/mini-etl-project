# Building ETL Process with a Mini Project

Hello everyone, I’m currently learning ETL process.

In this project, We’ll cover:

- How to extract CSV data from GitHub
- How to create Docker Compose file for python, mariadb and mongodb
- How to apply transform technique with python
- How to load final data to MongoDB
- Finally we add airflow for manage all this process.

![ETL_project_airflow](https://github.com/user-attachments/assets/589aec53-1016-43af-ab97-e6cfca6e5641)

You can find details of this article from the link : [Medium Post](https://medium.com/@merTaner/mini-etl-project-93e9a67c4139)

## Tools / Softwares Versions

|Tool|Version|Description|
| ------ | ------ | ----------- |
|Docker | 20.10.22 | Containerization platform |
|Docker Compose |v2.15.1|Tool for defining and running multi-container Docker applications|
|Postgres|Postgres:15|Open-source relational database for airflow|
|Airflow|2.10.3|Workflow automation and scheduling tool|
|Python | 3.11-slim| Programing language |
|MariaDb| 11.6     | Relational Database |
|MongoDB| 8.0      | NoSQL Database |

## Prerequisites

- Docker Desktop
- Python

## How To Run

1. First, create a Docker network to connect the containers:

    ```docker network create --subnet=172.80.0.0/16 dahbest```

2. Then, start the containers:

    ```docker-compose up -d --build ```

3. Access to localhost:8080

    Enter your username (you can change docker-compose env) : (default) mert

    Enter password : (default) 4444

4. Admin > Connections > Add new record  (if not exists)

    ```
    Connection Id : python_ssh
    Connection Type : SSH
    Host : Python
    Username : root
    Password : mertmert
    Port : 22
    ```

## If airflow-scheduler not working and throw error

Error like this : raise util.CommandError(resolution) from re
alembic.util.exc.CommandError: Can't locate revision identified by '5f2621c13b39'

1. Connect postgres container

    ``` docker exec -it posgresql-container psql -U mert -d airflow ```

2. Change value of the version_num

    ``` 
    UPDATE alembic_version
    SET version_num = '22ed7efa9da2'
    WHERE version_num = '5f2621c13b39'; 
    ```

