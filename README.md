# Metacritic API

Fetchs game detail from [http://www.metacritic.com](http://www.metacritic.com/game/playstation-4). More details in [tests](./tests/README.md)

## Run
* With `docker-compose`
```
## Review docker-compose.yml and start the deployment
$ docker-compose up -d --build
$ cd tests
$ python3 test.py
```
* With `cli`
```
$ pip3 install -e .
$ export PORT=8081
$ export URL=http://www.metacritic.com/game/playstation-4
$ metacritic_api 
INFO:Serving on http://0.0.0.0:8081
```
## More Details
* This application is written in Python Flask packed in pypi style, fetch game details and exposes 2 GET HTTP methods(More details in [tests](./tests/README.md))
* The application internally uses `waitress` server to serve requests.
* In `docker-compose` deployment, the nginx container acts as proxy which configuration can be seen[here](/nginx-proxy.conf) for metacritic-api container

## Tests
Please refer [tests](./tests/README.md) directory

## Tear Down
* `docker-compose`
```
$ docker-compose down
```
* `cli`
```
$ pip3 uninstall metacritic_api
```
