import math
from pyspark import SparkContext
from pyspark.sql import SparkSession
from os import system
from sparkClass import rdd_model


if __name__ == "__main__":
    
    spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)

    metadata = spark.read.format("com.mongodb.spark.sql.DefaultSource").load().rdd
    metadata.saveAsTextFile("hdfs://localhost:9000/user/hadoop/meta/")