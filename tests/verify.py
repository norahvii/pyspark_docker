from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("GPU-enabled-spark") \
    .config("spark.rapids.sql.enabled", "true") \
    .getOrCreate()

# Check if GPU is available
print(spark.sparkContext.getConf().getAll())
