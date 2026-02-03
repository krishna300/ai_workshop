### Useful docker commands for repo setup

docker container prune
docker rmi <image_id>

docker-compose up --build
docker-compose restart

docker exec -it basics_container bash
uv add pydantic

### Extra (Mostly not needed)

uv freeze > requirements.txt
uv add -r requirements.txt

### Steps to run this repo

1. Git clone the Repo
2. Docker compose build and up

You are all set !!
Note : Make sure your local system has docker setup installed and running !!
