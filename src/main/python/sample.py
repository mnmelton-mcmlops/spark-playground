import sys, os
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, Catalog
from pyspark.sql import DataFrame, DataFrameStatFunctions, DataFrameNaFunctions
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql.types import Row
from subprocess import check_output

SPARK_DRIVER_HOST = check_output(["hostname", "-i"]).decode(encoding="utf-8").strip()
print(SPARK_DRIVER_HOST)
spark_conf = SparkConf()
spark_conf.setAll([
    ('spark.master', 'spark://spark:7077'),
    ('spark.app.name', 'myApp'),
    ('spark.submit.deployMode', 'client'),
    ('spark.ui.showConsoleProgress', 'true'),
    ('spark.eventLog.enabled', 'false'),
    ('spark.executor.memory', '1G'),
    ('spark.logConf', 'false'),
    ('spark.driver.bindAddress', '0.0.0.0'),
    ('spark.driver.host', SPARK_DRIVER_HOST)
])

spark_sess          = SparkSession.builder.config(conf=spark_conf).getOrCreate()
spark_ctxt          = spark_sess.sparkContext
spark_reader        = spark_sess.read
spark_streamReader  = spark_sess.readStream
spark_ctxt.setLogLevel("DEBUG")

myDF  = spark_sess.createDataFrame([Row(col0=0, col1=1, col2=2),
                                    Row(col0=3, col1=1, col2=5),
                                    Row(col0=6, col1=2, col2=8)])

myGDF = myDF.select('*').groupBy('col1')
myDF.createOrReplaceTempView('mydf_as_sqltable')
print(myDF.collect())
myGDF.sum().show()
#
spark_sess.stop();
quit()
