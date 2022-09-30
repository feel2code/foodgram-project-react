<h1><a target="_blank" href="https://github.com/feel2code/foodgram-project-react/">Проект Foodgram Продуктовый помощник</a></h1>

![Foodgram workflow](https://github.com/feel2code/foodgram-project-react/actions/workflows/main.yml/badge.svg)

#### Проект запущен по адресу http://foodgramhelper.ddns.net/

## Описание
Проект Foodgram «Продуктовый помощник».
Сервис создан для публикации рецептов, добавления понравившихся рецептов в список «Избранное»,
подписок на публикации других пользователей.
Также доступен функционал загрузки списка продуктов, необходимых для приготовления блюд по выбранным рецептам.

## GitHub Workflow secrets
```Settings - Secrets - Actions secrets```
```
DOCKER_USERNAME = имя пользователя в DockerHub
DOCKER_PASSWORD = пароль пользователя в DockerHub
HOST = публичный ip-адрес сервера
USER = пользователь для подключения к серверу
SSH_KEY = приватный ssh-ключ
```

## Переменные окружения
``` infra/.env ```
```
DB_ENGINE=django.db.backends.postgresql  # движок БД
DB_NAME=postgres  # имя БД
POSTGRES_USER=postgres  # логин для подключения к БД
POSTGRES_PASSWORD=postgres  # пароль для подключения к БД
DB_HOST=db  # название контейнера
DB_PORT=5432  # порт для подключения к БД
ALLOWED_HOSTS=*, localhost # разрешенные хосты
SECRET_KEY=key # секретный ключ приложения django
```

## Запуск проекта
#### Клонируем репозиторий, создаем и активируем виртуальное окружение (GNU/Linux или Mac):
```bash
git clone https://github.com/feel2code/foodgram-project-react && cd foodgram-project-react && python3 -m venv venv && source venv/bin/activate
```
#### для Windows
```bash
git clone https://github.com/feel2code/foodgram-project-react && cd foodgram-project-react && python3 -m venv venv && source venv/Scripts/activate
```

#### Обновляем pip и устанавливаем зависимости:
```bash
python -m pip install --upgrade pip && pip install -r backend/requirements.txt
```

#### Переходим в директорию с файлом docker-compose.yaml:
```bash
cd infra
```

#### Запуск docker-compose:
```bash
docker-compose up -d --build
```

#### После успешной сборки на сервере выполняем команды:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

#### Применяем миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

#### Команда для заполнения базы тестовыми данными:
```bash
docker-compose exec backend python manage.py loaddata db.json
```

#### Загружаем данные в базу данных:
```bash
docker-compose exec backend python manage.py load_ingredients ingredients.json && docker-compose exec backend python manage.py load_ingredients tags.json
```

#### Создаем суперпользователя Django:
```bash
docker-compose exec backend python manage.py createsuperuser
```

### Ссылки на проект:
Проект после запуска будет доступен по адресу - http://localhost/

Админ панель будет доступна по адресу - http://localhost/admin/

Документация API по адресу - http://localhost/api/docs/

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

## Запуск проекта на сервере
#### Подключение по SSH
```bash
ssh <username>@<ip-adress>
```

#### Обновляем пакеты:
```bash
sudo apt update -y && sudo apt upgrade -yy 
```

#### Устанавливаем docker и docker-compose:
```bash
sudo apt install docker docker-compose 
```

#### Устанавливаем Postgres DB:
```bash
sudo apt install postgresql postgresql-contrib
```

Подготовьте файл ```nginx.conf``` вписав в строке ```server_name``` публичный ip сервера.
Затем скопируйте директорию рекурсивно на сервер с помощью scp.
```bash
scp -r infra <username>@<host>:/infra
```

Запуск проекта осуществляется аналогично процессу на локальной машине,
за исключением того, что все команды должны вводится через ```sudo```

## Использованные технологии:
```bash, python 3.7, django 2.2, django REST Framework, postgreSQL 13.0, docker,
Docker Hub, Nginx, Gunicorn 20.0.4, GitHub Actions, Yandex.Cloud.```

## Автор проекта
[feel2code](https://t.me/feel2code)
