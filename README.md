## Init project:
```
sudo apt update && sudo apt install python3.11
virtualenv venv -p python3.11
source venv/bin/activate
pip install poetry
poetry install
alembic upgrade head
```

## Adding new dependency:
```
poetry add <package_name>[<package_extras>]@^<package_version>
poetry install
```


## Update dependencies
```
poetry update
```


## Run application
```
docker compose up -d
source venv/bin/activate
python src/app.py
```

## Check code:
```
./check.sh
```

## Run tests:
```
pytest tests/unit_tests
pytest tests/integration_tests
```

## Migrations:
* Autogenerate migration: `alembic revision --autogenerate -m "<YOUR_MESSAGE_HERE>"`
* Apply migrations: `alembic upgrade head`
* Revert migration: `alembic downgrade head-1`
* Check migrations history: `alembic history`
* Check migration heads: `alembic heads`
