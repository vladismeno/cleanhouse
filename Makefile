DOCKER_COMPOSE = docker-compose
MANAGE_PY = $(DOCKER_COMPOSE) exec web python manage.py

# Команда для запуска контейнеров Docker
up:
	$(DOCKER_COMPOSE) up --build

# Команда для остановки и удаления контейнеров Docker
down:
	$(DOCKER_COMPOSE) down

makemigrations:
	$(MANAGE_PY) makemigrations

# Команда для применения миграций Django
migrate:
	$(MANAGE_PY) migrate

# Команда для создания суперпользователя Django
createsuperuser:
	$(MANAGE_PY) createsuperuser

# Команда для сбора статических файлов Django
collectstatic:
	$(MANAGE_PY) collectstatic --no-input

# Команда для запуска тестов Django
test:
	$(MANAGE_PY) test

# Команда для проверки стиля кода с помощью pylint
lint:
	pylint .

# Команда для очистки миграций Django
cleanmigrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
