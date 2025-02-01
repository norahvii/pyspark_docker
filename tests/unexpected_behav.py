from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors

features_df = spark.createDataFrame([
    (1,Vectors.dense([10.0,10000.0, 1.0]),),
    (2,Vectors.dense([20.0,30000.0, 2.0]),),
    (3,Vectors.dense([30.0,40000.0, 3.0]),)
],["id","features"])

feature_scaler = MinMaxScaler(inputCol="features",outputCol="sfeatures")
smodel = feature_scaler.fit(features_df)
sfeatures_df = smodel.transform(features_df)

sfeatures_df.select("features", "sfeatures").show(truncate=False)

# Returns:
# +------------------+--------------------+
# |          features|           sfeatures|
# +------------------+--------------------+
# |[10.0,10000.0,1.0]|           (3,[],[])|
# |[20.0,30000.0,2.0]|[0.5,0.6666666666...|
# |[30.0,40000.0,3.0]|       [1.0,1.0,1.0]|
# +------------------+--------------------+

# Expected:
# +------------------+--------------------+
# |          features|           sfeatures|
# +------------------+--------------------+
# |[10.0,10000.0,1.0]|       [0.0,0.0,0.0]|
# |[20.0,30000.0,2.0]|[0.5,0.6666666666...|
# |[30.0,40000.0,3.0]|       [1.0,1.0,1.0]|
# +------------------+--------------------+