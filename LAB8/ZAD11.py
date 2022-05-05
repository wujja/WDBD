from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r'[\w]+')

class MRMostUsedWord(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
            combiner=self.combiner_count_words,
            reducer=self.reducer_find_max_word)
            #MRStep(reducer=self.reducer_find_max_word)
        ]
        
    def mapper_get_words(self, _ , line):
        for number in line.splitlines():
            salary = int(float(number.split(',')[-2].replace("$","")))
            #salary = [x for x in number]
            yield(salary, 1)

    def combiner_count_words(self, word, counts):
        yield None, (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield None, (sum(counts), word)

    def reducer_find_max_word(self, _, counts):
        self.max_list = []
        for z in counts:
            if(len(self.max_list) < 10):
                self.max_list.append(z)
            elif(z > min(self.max_list)):
                self.max_list.remove(min(self.max_list))
                self.max_list.append(z)
        for i in range(10):
            yield self.max_list[i]


if __name__ == '__main__':
    MRMostUsedWord.run()