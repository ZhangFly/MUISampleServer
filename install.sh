#!/bin/bash

REMOTE_PATH=https://raw.githubusercontent.com/ZhangFly/MUISampleServer/master
LOCAL_PATH=/usr/local/MUISample/Server

curl "$REMOTE_PATH"/auto-deploy.sh -o "$LOCAL_PATH"/auto-deploy.sh "$REMOTE_PATH"/docker-compose.yaml -o "$LOCAL_PATH"/docker-compose.yaml
