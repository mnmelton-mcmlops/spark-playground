mb heart
mb cities
mb iris
cp data/heart.csv heart/heart.csv
cp data/iris.csv iris/iris.csv
cp data/cities.csv cities/cities.csv



#docker run --rm -it --name minio-client     --env MINIO_SERVER_HOST="minio"     --env MINIO_SERVER_ACCESS_KEY="minio-root-user"  --network spark-playground_spark    --env MINIO_SERVER_SECRET_KEY="minio-root-password" bitnami/minio-client  --  mb supreme

