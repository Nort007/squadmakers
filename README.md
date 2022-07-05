# How To Use:


#### LAUNCH DOCKER COMPOSE LOCAL VERSION

* **launch**: `docker-compose -f 'docker-compose.local.yml' --env-file .env.example up -d`


#### IMPLEMENT THE MIGRATIONS BY ALEMBIC

After install some containers launch this command:
* **launch**: `docker exec -ti api_squadmaker sh -c "python3 -m alembic upgrade head"`
***

# Structure

#### Endpoints:

* api:
  * joke
  * mathematico

#### Models:
* db:
  * jokes
  * enums - enum variables for jokes
  * base - general added model to other some models

#### Configs
* core

#### Schemas
* Schema for using pydantic for the joke model

#### Docs
* docs: - yaml for swagger
