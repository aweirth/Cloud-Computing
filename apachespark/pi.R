# Load required library
library(SparkR)

# Initialize SparkSession
sparkR.session(appName = "R-Pi")

# Define the number of partitions (equivalent to Python's `partitions` argument)
partitions <- as.integer(commandArgs(trailingOnly = TRUE)[1]) # Read from command line argument
n <- 100000 * partitions

# Function to calculate if a point is inside the circle
calculate_pi <- function(_: integer) {
  x <- runif(1, -1, 1)
  y <- runif(1, -1, 1)
  return(ifelse(x^2 + y^2 <= 1, 1, 0))
}

# Calculate the count of points inside the circle using Spark
count <- SparkR:::parallelize(sc, seq_len(n), partitions) %>%
  SparkR:::sapply(calculate_pi) %>%
  SparkR:::reduce(function(a, b) a + b)

# Print the approximation of pi
cat(sprintf("Pi is roughly %.6f\n", 4 * count / n))

# Stop the SparkSession
sparkR.session.stop()
