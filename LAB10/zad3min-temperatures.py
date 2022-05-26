'''
Pierwszy sposob
'''
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    temperature = float(fields[3])
    return (temperature)

lines = sc.textFile("/input/temp.csv")
parsedLines = lines.map(parseLine)

tempTuple = parsedLines.map(lambda x: (x, 1)) # przydziel 1 (temp, 1)
tempNum = tempTuple.reduceByKey(lambda x, y: x + y) # reduce po temp
tempNum = tempNum.sortByKey() # sort by temp
results = tempNum.collect(); # aby mozna bylo wyswietlic

tempNum.saveAsTextFile('/output') # zapisz na hdfs

for result in results:
    print(f'{round(result[0],1)}    {result[1]}')

    
