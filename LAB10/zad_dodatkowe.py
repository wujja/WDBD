from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf=conf)

def parseWords(line):
    words = line.split()
    words = [word.strip("'").strip(',').strip('.').strip('?').strip('!').strip('*') for word in words]
    return words


lines = sc.textFile('/input/opowiesc.txt')
parsedLines = lines.flatMap(parseWords) # Wszystkie wyrazy razem, zwykle map dodaje kazdy wiersz do odzielnej listy

wordsTuple = parsedLines.map(lambda x: (x, 1)) # przypisujemy 1 do slowa (word, 1)
wordsCounts = wordsTuple.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False) # redukcja po word. sort po ilosci, False=desc

wordsCounts.saveAsTextFile('/output2')

for line in wordsCounts.collect():
    print(line)