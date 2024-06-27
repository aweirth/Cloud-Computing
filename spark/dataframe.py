"""
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PythonSparkDataFrameExample") \
    .getOrCreate()

# Create a simple local data frame
local_data = [("John", 19), ("Smith", 23), ("Sarah", 18)]
schema = ["name", "age"]
localDF = spark.createDataFrame(local_data, schema)

# Print its schema
localDF.printSchema()

# Create a DataFrame from a JSON file
path = "{}/examples/src/main/resources/people.json".format(spark.sparkContext._gateway.jvm.java.lang.System.getenv("SPARK_HOME"))
peopleDF = spark.read.json(path)

# Print its schema
peopleDF.printSchema()

# Register this DataFrame as a table
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# Call collect to get a local data frame
teenagersLocalDF = teenagers.collect()

# Print the teenagers in our dataset
for row in teenagersLocalDF:
    print(row)

# Stop the SparkSession
spark.stop()
