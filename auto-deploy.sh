#!/bin/bash

DOCKER_COMPOSE_DIR=/usr/local/MUISample/Server/docker-compose.yml

docker-compose -f "$DOCKER_COMPOSE_DIR" pull
docker-compose -f "$DOCKER_COMPOSE_DIR" stop
docker-compose -f "$DOCKER_COMPOSE_DIR" up -d