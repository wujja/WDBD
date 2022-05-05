from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r'[\w]+')

class MRMostUsedWord(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_salary,
            combiner=self.combiner_count_salary,
            reducer=self.reducer_find_max_salary)#,
            #MRStep(reducer=self.reducer_find_max_word)
        ]
        
    def mapper_get_salary(self, _ , line):
        for number in line.splitlines():
            salary = int(float(number.split(',')[-2].replace("$","")))
            yield(salary, 1)

    def combiner_count_salary(self, salary, counts):
        yield None, (salary, sum(counts))

    #tego nie uzywam
    def reducer_count_salary(self, salary, counts):
        yield None, (sum(counts), salary)

    def reducer_find_max_salary(self, _, salary):
        self.max_list = []
        for z in salary:
            if(len(self.max_list) < 10):
                self.max_list.append(z)
            elif(z > min(self.max_list)):
                self.max_list.remove(min(self.max_list))
                self.max_list.append(z)
        for i in range(10):
            yield self.max_list[i]


if __name__ == '__main__':
    MRMostUsedWord.run()