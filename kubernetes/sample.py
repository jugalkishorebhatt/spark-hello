from pyspark import SparkContext, SparkConf
from my-module import myfn

if __name__ == '__main__':
    conf = SparkConf().setAppName("app")
    sc = SparkContext(conf=conf)
    words = 'the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog'
    sc = SparkContext()
    seq = words.split()
    data = sc.parallelize(seq)
    counts = data.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).collect()
    dict(counts)
    sc.stop()
