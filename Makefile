command:
	alembic init -t async alembic
	alembic revision --autogenerate -m 'initial'
	alembic upgrade head