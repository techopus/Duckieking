#!/bin/bash
docker build -t duckiequeen .
docker rm duckiequeen_dev
docker run -dt --name duckiequeen_dev duckiequeen
docker exec -it duckiequeen_dev /bin/bash
