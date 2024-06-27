# dataframe.py - Spark Python example for DataFrame operations

from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Spark DataFrame Example").getOrCreate()

# Create a simple local DataFrame
data = [("John", 19), ("Smith", 23), ("Sarah", 18)]
columns = ["name", "age"]
localDF = spark.createDataFrame(data, columns)

# Print its schema
localDF.printSchema()

# Create a DataFrame from a JSON file
path = "{}/examples/src/main/resources/people.json".format(spark.sparkContext.getConf().get("spark.home"))
peopleDF = spark.read.json(path)

# Print its schema
peopleDF.printSchema()

# Register this DataFrame as a table
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql method
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# Call collect to get a local DataFrame
teenagersLocalDF = teenagers.collect()

# Print the teenagers in our dataset
for row in teenagersLocalDF:
    print(row['name'])

# Stop the SparkSession
spark.stop()
