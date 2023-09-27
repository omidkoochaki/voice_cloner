build:
	docker compose -f local.yml build

makemigrations:
	docker compose -f local.yml run --rm api python3 manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python3 manage.py migrate

start:
	docker compose -f local.yml up

down:
	docker compose -f local.yml down

down-v:
	docker compose -f local.yml down -v

superuser:
	docker compose -f local.yml run --rm api python3 manage.py createsuperuser