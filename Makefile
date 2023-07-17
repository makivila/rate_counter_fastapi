build:
	docker-compose build

run:
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs -f
