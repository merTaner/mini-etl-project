# Building ETL Process with a Mini Project

### Hello everyone, I’m currently learning ETL process.

#### In this project, We’ll cover:

- How to extract CSV data from GitHub
- How to create Docker Compose file for python, mariadb and mongodb
- How to apply transform technique with python
- How to load final data to MongoDB

#### You can find details of this article from the link : [Medium Post](https://medium.com/@merTaner/mini-etl-project-93e9a67c4139)

### Tools / Softwares Versions
---

|Tool|Version|Description|
| ------ | ------ | ----------- |
|Docker | 20.10.22 | Containerization platform |
|Python | 3.11-slim| Programing language |
|MariaDb| 11.6     | Relational Database |
|MongoDB| 8.0      | NoSQL Database |


### Prerequisites
---
- Docker Desktop
- Python

### How To Run
---
First, create a Docker network to connect the containers:

```docker network create --subnet=172.80.0.0/16 dahbest```

Then, start the containers:

```docker-compose up -d --build ```