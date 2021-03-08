.PHONY: setup test run help

setup:
	@echo 'Installing dependencies from API'
	@echo 'Flask + SQLite3'
	docker-compose build api
	@echo 'Setup finished'

test:
	@echo 'Running unit tests'

run:
	@echo 'Starting application'
	docker-compose up api

help:
	@echo 'Available options:'
	@echo 'setup :: Install dependencies related to application'
	@echo 'run :: Start application'
	@echo 'test :: Perform unit tests on application'
