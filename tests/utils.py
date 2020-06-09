"""Utils where we all dump crap that we don't know how to organize."""

from pyspark.sql import DataFrame, SparkSession

from tests.mock_data import SCHEMA, RAW_DATA

spark = SparkSession.builder.getOrCreate()

def load_mock_data_func(*args, **kwargs):
    return spark.createDataFrame(RAW_DATA, SCHEMA)
