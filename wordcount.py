import sys
from pyspark.sql import SparkSession
 
if __name__ == "__main__":
 spark = SparkSession.builder.appName('abc').getOrCreate()
 words = 'the quick brown fox jumps over the\
        lazy dog the quick brown fox jumps over the lazy dog'
 sc = spark.SparkContext()
 seq = words.split()
 data = sc.parallelize(seq)
 counts = data.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).collect()
 dict(counts)
 sc.stop() 
