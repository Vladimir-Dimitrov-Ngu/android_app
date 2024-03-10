# Проект по автоматизации детекции вирусного ПО



<div align="center">
    
  <a href="https://github.com/Vladimir-Dimitrov-Ngu/CV_RIT/issues">![GitHub issues](https://img.shields.io/github/issues/e0xextazy/nlp_huawei_new2_task)</a>
  <a href="https://github.com/Vladimir-Dimitrov-Ngu/CV_RIT/blob/master/LICENSE">![GitHub license](https://img.shields.io/github/license/e0xextazy/nlp_huawei_new2_task?color=purple)</a>
  <a href="https://github.com/psf/black">![Code style](https://img.shields.io/badge/code%20style-black-black)</a>
    
</div>



#### Languages and Tools:
 
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![fastapi](https://img.shields.io/badge/fastapi-3670A0?style=for-the-badge&logo=fastapi&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![dash](https://img.shields.io/badge/dash-3670A0?style=for-the-badge&logo=dash&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![sqlalchemy](https://img.shields.io/badge/sqlalchemy-3670A0?style=for-the-badge&logo=sqlalchemy&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![sklearn](https://img.shields.io/badge/sklearn-3670A0?style=for-the-badge&logo=sklearn&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![redis](https://img.shields.io/badge/redis-3670A0?style=for-the-badge&logo=redis&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![catboost](https://img.shields.io/badge/catboost-3670A0?style=for-the-badge&logo=catboost&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![jwt](https://img.shields.io/badge/jwt-3670A0?style=for-the-badge&logo=jwt&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Docker](https://img.shields.io/badge/docker-3670A0?style=for-the-badge&logo=docker&logoColor=ffdd53)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-3670A0?style=for-the-badge&logo=jupyter&logoColor=ffdd53)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Celery](https://img.shields.io/badge/celery-3670A0?style=for-the-badge&logo=celery&logoColor=ffdd53)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Git](https://img.shields.io/badge/git-3670A0?style=for-the-badge&logo=git&logoColor=ffdd53)](https://github.com/Vladimir-Dimitrov-Ngu)

## Структура Проекта
```
project/
|-- backend/ -- серверная часть
|   |-- api/
|   |   |-- routes
|   |   |-- queue
|   |   |-- controllers
|   |   |-- config
|   |   |-- database
|   |   |-- ml
|   |   |-- models
|   |-- app.py

|-- frontend/ - клиентская часть
|   |-- assets
|   |-- callback
|   |-- config
|   |-- controllers
|   |-- statis
|   |-- templates
|   |-- app_main_menu.py
|   |-- app_register.py
|-- README.md
|-- Dockerfile
|-- LICENSE
|-- .gitignore
|-- main.py - точка входа в приложение
```

## Полное описание проекта

### Серверная часть (backend):

- API: Модуль для обработки запросов с разделением на маршруты, обработчики и контроллеры.

- Queue: Реализация очереди запросов для эффективной обработки данных.

- Controllers: Логика обработки запросов, включая взаимодействие с базой данных и модулем машинного обучения.

- Config: Конфигурационные файлы для API.

- Database: Модуль для работы с базой данных.

- ML (Machine Learning): Модуль для реализации алгоритмов машинного обучения.

- Models: Определение моделей данных для хранения информации в базе данных.

#### app.py: Основной файл серверного приложения.

### Клиентская часть (frontend):

- Assets: Ресурсы, такие как изображения и шрифты.

- Callback: Обработчики обратных вызовов.

- Config: Конфигурационные файлы клиента.

- Controllers: Контроллеры для управления 
представлением.

- Static: Статические файлы, такие как CSS, JS, и изображения.

- Templates: HTML-шаблоны для отображения информации.

#### app_main_menu.py: Модуль главного меню приложения.

#### app_register.py: Модуль регистрации.

### API
- POST /api/login

Этот метод принимает POST-запрос по пути "/api/login".

- POST /api/predict

Этот метод также принимает POST-запрос по пути "/api/predict". Запускает задачу create_job(), которая в свою очередь добавляет задачу в очередь

- GET /api/money

Этот метод принимает GET-запрос по пути "/api/money"

### Демо
[Демо](https://drive.google.com/file/d/1xM3eyfHUk7nPPBfEhBKGVAPC0kdD_WVk/view?usp=sharing)


### Дальнешний разработки 
- Мобильное Приложение
- Улучшение Алгоритмов Детекции