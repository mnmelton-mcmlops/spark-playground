#!/bin/sh

mc alias set minio http://$MINIO_SERVER_HOST:9000 $MINIO_SERVER_ACCESS_KEY $MINIO_SERVER_SECRET_KEY

mc mb minio/heart
mc mb minio/cities
mc mb minio/iris
mc cp ./data/heart.csv minio/heart/heart.csv
mc cp ./data/iris.csv minio/iris/iris.csv
mc cp ./data/cities.csv minio/cities/cities.csv