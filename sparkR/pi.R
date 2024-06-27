#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Load required library
library(SparkR)

# Initialize SparkSession
sparkR.session(appName = "R-Pi")

# Read partitions value from command line argument or default to 2
partitions <- as.integer(commandArgs(trailingOnly = TRUE)[1]) # Read from command line argument
n <- 100000 * partitions

# Function to calculate if a point is inside the circle
calculate_pi <- function(_: integer) {
  x <- runif(1, -1, 1)
  y <- runif(1, -1, 1)
  return(ifelse(x^2 + y^2 <= 1, 1, 0))
}

# Calculate the count of points inside the circle using SparkR
count <- SparkR:::parallelize(sc, seq_len(n), partitions) %>%
  SparkR:::sapply(calculate_pi) %>%
  SparkR:::reduce(function(a, b) a + b)

# Print the approximation of pi
cat(sprintf("Pi is roughly %.6f\n", 4 * count / n))

# Stop the SparkSession
sparkR.session.stop()

