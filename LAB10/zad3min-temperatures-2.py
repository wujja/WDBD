'''
Drugi sposob
'''
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    temperature = float(fields[3])
    return (temperature)

lines = sc.textFile("/input/temp.csv")
parsedTemp = lines.map(parseLine).countByValue() 

#Nie wiem jak wgrac to na HTFS, bo parsedTemp nie jest to RDD
#parsedTemp.saveAsTextFile('/output')
# ok mozna, metoda countByValue() zwraca dict, nalezy utworzyc plik RDD i wtedy zapisac
justToSave = sc.parallelize(sorted(parsedTemp.items())).saveAsTextFile('output') # Zapis


for temp, count in sorted(parsedTemp.items()):
    print(f"{temp}  {count}")

    
