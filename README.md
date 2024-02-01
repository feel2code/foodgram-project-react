# [Foodgram Project - Food Assistant](https://github.com/feel2code/foodgram-project-react/)

## Description
"Foodgram" it's a study project from Yandex.Practicum training course - food assistant.

The service is designed for publishing recipes, adding favorite recipes to the favorites list, and subscribing to publications of other users. It also includes the functionality to download a list of ingredients needed to prepare dishes from selected recipes.

### GitHub Workflow secrets

- *DOCKER_USERNAME*: DockerHub username
- **DOCKER_PASSWORD*: DockerHub password
- *HOST*: public IP address of the server
- *USER*: username for connecting to the server
- *SSH_KEY*: private SSH key

### Environment Variables

- *DB_ENGINE*: django.db.backends.postgresql  # database engine
- *DB_NAME*: postgres  # database name
- *POSTGRES_USER*: postgres  # login to connect to the database
- *POSTGRES_PASSWORD*: postgres  # password to connect to the database
- *DB_HOST*: db  # container name
- *DB_PORT*: 5432  # port to connect to the database
- *ALLOWED_HOSTS*: *, localhost # allowed hosts
- *SECRET_KEY*: key # Django application secret key

## Project Setup
```bash
# Clone the repository and set up a virtual environment
git clone https://github.com/feel2code/foodgram-project-react && cd foodgram-project-react && python3 -m venv venv && source venv/bin/activate
# For Windows
git clone https://github.com/feel2code/foodgram-project-react && cd foodgram-project-react && python3 -m venv venv && source venv/Scripts/activate

# Update pip and install dependencies
python -m pip install --upgrade pip && pip install -r backend/requirements.txt

# Navigate to the directory with the docker-compose.yaml file
cd infra

# Run docker-compose
docker-compose up -d --build

# After a successful build on the server, execute the following commands
docker-compose exec backend python manage.py collectstatic --noinput

# Apply migrations
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput

# Command to populate the database with test data
docker-compose exec backend python manage.py loaddata db.json

# Load data into the database
docker-compose exec backend python manage.py load_ingredients ingredients.json && docker-compose exec backend python manage.py load_ingredients tags.json

# Create a Django superuser
docker-compose exec backend python manage.py createsuperuser
```

## Project Links:
After launch, the project will be available at - http://localhost/

The admin panel will be accessible at - http://localhost/admin/

API documentation can be found at - http://localhost/api/docs/

### Stopping Containers:
```bash
docker-compose down -v
```

## Running the Project on the Server
### Connecting via SSH

```bash
ssh <username>@<ip-address>
```

### Updating Packages:

```bash
sudo apt update -y && sudo apt upgrade -yy
```

### Installing Docker and Docker Compose:

```bash
sudo apt install docker docker-compose
```

### Installing Postgres DB:

```bash
sudo apt install postgresql postgresql-contrib
```

Prepare the nginx.conf file by entering the public server IP in the server_name line. Then copy the directory recursively to the server using scp.

```bash
scp -r infra <username>@<host>:/infra
```

Running the project is similar to the process on the local machine, except that all commands should be entered with sudo.


## Technologies Used:

*bash, Docker Hub, Nginx, Gunicorn 20.0.4, GitHub Actions, Yandex.Cloud.*
