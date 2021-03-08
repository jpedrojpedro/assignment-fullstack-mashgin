## Mashgin :: Full-Stack Take Home Assignment

#### Goal

Create a simple checkout web app with client app and server API.

The users should be able to see menu items fetched from the web API, add/remove items to their cart, fill a payment form
and submit the order to the web API.


The payment doesn't need to be processed and the endpoint can just store the order in a file or db and return a
successful response.

#### Dependencies

The project has the following **backend** dependencies:
  - [Docker](https://www.docker.com) & [Docker Compose](https://docs.docker.com/compose/) - main dependencies
    - [Flask](https://palletsprojects.com/p/flask/)
    - [Peewee](http://docs.peewee-orm.com/en/latest/)
    - [SQLite3](https://www.sqlite.org/index.html)

Also the project has the following **fronted** dependencies (_TBD_):
  - [Vue.js](https://vuejs.org)

#### Architecture

_TBD_

#### Tests

_TDB_

#### How to use it

There is a `Makefile` to facilitate the project's usage. Here are the available commands:

```
make setup  # Install dependencies related to application
make run    # Start application
make test   # Perform unit tests on application
```

#### Directory Structure

The `docker-compose.yml` file has two declared services: api e test.

Inside `docker/Dockerfile` backend dependencies are declared - libs.

Folder `app/` is the main directory of the project.
Inside it, there are python files each one with its own responsibility.
Here follows in details:

- `init.py`: file with global configurations of the project
- `main.py`: file responsible to start the application
- `models.py`: file with Python classes related to data layer (Peewee ORM + SQLite3 communication)
- `tests.py`: _TBD_
- `views.py`: controller file with all API endpoints available
