from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

spark = SparkSession.builder \
    .appName("GPU-enabled-spark") \
    .config("spark.rapids.sql.enabled", "true") \
    .config("spark.rapids.sql.concurrentGpuTasks", "2") \
    .config("spark.executor.resource.gpu.amount", "1") \
    .config("spark.task.resource.gpu.amount", "1") \
    .config("spark.executor.cores", "1") \
    .master("local[1]") \
    .getOrCreate()

# Test GPU-specific operation
df = spark.createDataFrame([(1, 2), (3, 4)], ["a", "b"])
df.select(expr("a + b").alias("sum")).show()