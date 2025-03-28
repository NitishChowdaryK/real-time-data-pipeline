from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Define schema
schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("timestamp", DoubleType()),
    StructField("security", StringType()),
    StructField("region", StringType()),
    StructField("value", DoubleType())
])

# Snowflake options
sfOptions = {
    "sfURL": "https://ynwbbwi-fib67654.snowflakecomputing.com",
    "sfUser": "Nitishchowdary22",
    "sfPassword": "Nitishchowdary@2002",
    "sfDatabase": "FINANCE_DB",
    "sfSchema": "TRANSACTIONS",
    "sfWarehouse": "COMPUTE_WH",
    "sfRole": "ACCOUNTADMIN"
}

spark = SparkSession.builder \
    .appName("KafkaToSnowflake") \
    .config("spark.jars.packages", 
       "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2,"
       "net.snowflake:spark-snowflake_2.12:2.11.0-spark_3.3,"
       "net.snowflake:snowflake-jdbc:3.13.22") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "host.docker.internal:9092") \
    .option("subscribe", "financial-logs") \
    .option("startingOffsets", "earliest") \
    .load()

parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .dropDuplicates(["transaction_id"])

def write_to_snowflake(batch_df, epoch_id):
    batch_df.write \
        .format("snowflake") \
        .options(**sfOptions) \
        .option("dbtable", "TRANSACTIONS_TABLE") \
        .mode("append") \
        .save()

parsed_df.writeStream \
    .foreachBatch(write_to_snowflake) \
    .start() \
    .awaitTermination()
