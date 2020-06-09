from pyspark.sql.types import StructType, StructField, IntegerType

SCHEMA = StructType(
    fields=[
        StructField("id", IntegerType(), False),
        StructField("x", IntegerType(), False),
    ]
)

RAW_DATA = [
    {'id': 0, 'x': 1},
    {'id': 1, 'x': 0},
    {'id': 2, 'x': 17},
    {'id': 3, 'x': 2},
    {'id': 4, 'x': 10},
    {'id': 5, 'x': 5},
    {'id': 6, 'x': 10},
    {'id': 7, 'x': 4},
    {'id': 8, 'x': 4},
    {'id': 9, 'x': 3}
]
