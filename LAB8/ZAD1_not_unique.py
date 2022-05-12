from mrjob.job import MRJob

class MRTop10Salary(MRJob):

    def mapper(self,_,line):
        for number in line.splitlines():
            salary = int(float(number.split(',')[-2].replace("$","")))
            yield(salary, 1)

    def combiner(self, number, counts):
        yield None, (number,sum(counts))

    def reducer(self, _, number):
        self.max_list = []
        for z in number:
            if(len(self.max_list) < 10):
                self.max_list.append(z)
            elif(z > min(self.max_list)):
                self.max_list.remove(min(self.max_list))
                self.max_list.append(z)
        self.max_list.sort()
        for i in range(10):
            yield self.max_list[i]
        

if (__name__ == '__main__'):
    MRTop10Salary.run()