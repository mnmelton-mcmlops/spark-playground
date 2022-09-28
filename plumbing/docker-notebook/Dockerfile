FROM docker.io/bitnami/spark:3.3

USER root

EXPOSE 8888

WORKDIR /opt/bitnami/spark/work

COPY cacert.pem /opt/bitnami/spark/venv/lib/python3.8/site-packages/pip/_vendor/certifi/
ENV VIRTUAL_ENV=/opt/bitnami/spark/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["jupyter-lab","--ip=0.0.0.0", "--allow-root"]


# docker run --rm -ti -u root -v $(pwd)/notebook_data/test.py:/bitnami/spark/test.py \
# --network spark-playground_spark -p 8888:8888 bitnami/spark:3.3 bash

# groupadd -g 1000 -o pyspark
# useradd -m -u 1000 -g 1000 -o -s /bin/bash pyspark

# su pyspark
# cd ~

# mkdir pyspark
# cd pyspark
# virtualenv .
# source bin/activate

# pip install pyspark
# pip install jupyterlab 
# pip install pandas
# pip install matplotlib

# jupyter-lab --ip=0.0.0.0