from statistics import mean
from mrjob.job import MRJob

class MRSalariesGroupBy(MRJob):

    def mapper(self,_, line):
        for number in line.splitlines():
            salary = int(float(number.split(',')[-2].replace('$','')))
            work_class = number.split(',')[2]
            yield (work_class, salary)

    def reducer(self, work_class, salary):
        yield (work_class,mean(salary))

if(__name__ == '__main__'):
    MRSalariesGroupBy.run()