#!/bin/sh

#mc alias set minio $MINIO_SERVER_HOST $MINIO_SERVER_ACCESS_KEY $MINIO_SERVER_SECRET_KEY

mc mb heart
mc mb cities
mc mb iris
mc cp ./data/heart.csv heart/heart.csv
mc cp ./data/iris.csv iris/iris.csv
mc cp ./data/cities.csv cities/cities.csv



#docker run --rm -it --name minio-client     --env MINIO_SERVER_HOST="minio"     --env MINIO_SERVER_ACCESS_KEY="minio-root-user"  --network spark-playground_spark    --env MINIO_SERVER_SECRET_KEY="minio-root-password" bitnami/minio-client  --  mb supreme

