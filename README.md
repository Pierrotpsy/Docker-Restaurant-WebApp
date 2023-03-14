# Docker-Restaurant-WebApp

## Project Description

This is a simple web application to view, add, modify and delete restaurants from a sample database.

## Project Goal

This project is a simple use of docker containers and docker compose to create a fully fledged app while keeping it containerized.
It uses four services : 
- mongodb database
- import service to seed the initial mongodb instance
- API as a backend flask application
- frontend as a simple flask application

All of these containers communicate with each other through docker bridge networks, and the database is made persistent by using a docker volume to host it.

## Installation

### Prerequisites
Make sure that docker is installed on your machine.

```shell
docker --version
```
If not installed, run:

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Make sure that you have docker compose installed.
````shell
docker compose version
````
### Installation

To install the project, simply download or fork this repository.


## Running the project
In your project folder, run:
```shell
docker compose build
```

This will create the images needed for the app and install all dependencies.

To launch the app itself, run:
```shell
docker compose up
```

You should be able to access the app on `localhost:8000`, `127.0.0.1:8000`, `192.168.0.3:8000`.

## Additional information