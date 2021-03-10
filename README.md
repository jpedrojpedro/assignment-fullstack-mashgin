## Mashgin :: Full-Stack Take Home Assignment

![](https://raw.githubusercontent.com/jpedrojpedro/assignment-fullstack-mashgin/master/app/static/simple-checkout.png)

### Goal

Create a simple checkout web app with client app and server API.

The users should be able to see menu items fetched from the web API, add/remove items to their cart, fill a payment form
and submit the order to the web API.

The payment doesn't need to be processed and the endpoint can just store the order in a file or db and return a
successful response.

### Dependencies

The project has the following **backend** dependencies:
  - [Docker](https://www.docker.com) & [Docker Compose](https://docs.docker.com/compose/) - main dependencies
    - [Flask](https://palletsprojects.com/p/flask/) - web server
    - [Peewee](http://docs.peewee-orm.com/en/latest/) - ORM
    - [SQLite3](https://www.sqlite.org/index.html) - database

Also the project has the following **fronted** dependencies:
  - [Vue.js](https://vuejs.org)

### How to use it

#### Backend

There is a `Makefile` to facilitate the project's usage. Here are the available commands:

```
make setup  # Install dependencies related to application
make run    # Start application
make test   # Perform unit tests on application
```

The web server will be running on `http://localhost:5000/`.

#### Frontend

Here are the available commands:

```
npm install    # Project setup
npm run serve  # Compiles and hot-reloads for development
npm run build  # Compiles and minifies for production
```

#### Navigating

- open browser and access `http://localhost:8080/`
  - we recommend to use Chrome because there is a problem with CORS
  - use this Chrome Extension called [Allow CORS](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf)

### Directory Structure

The `docker-compose.yml` file has two declared services: api e test.

Inside `docker/Dockerfile` backend dependencies are declared - libs.

Folder `app/` is the main directory of the backend part of the project.
Inside it, there are python files each one with its own responsibility.
Here follows in details:

- `init.py`: file with global configurations of the project
- `main.py`: file responsible to start the application
- `models.py`: file with Python classes related to data layer (Peewee ORM + SQLite3 communication)
- `views.py`: controller file with all API endpoints available

Folder `app-front` is the main directory of the frontend part of the project.
The structure follows Vue.js recommendation.
Here follows in details:

- `src/components`: one component called `Product.vue` was developed to display the menu options as cards
- `src/App.vue`: the main page of the frontend application
