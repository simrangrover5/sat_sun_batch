
class Statistics:
    def __init__(self,data):
        self.data = data
        
    def mean(self):
        m = sum(self.data)/len(self.data)
        return m
    
    def median(self):
        self.data.sort()
        if len(self.data)%2 == 0:
            n1 = len(self.data)//2
            n2 = (len(self.data) + 2)//2
            m = (self.data[n1] + self.data[n2])/2
            return m
        else:
            n1 = (len(self.data) + 1)//2
            m = self.data[n1]
            return m
    def mode(self):
        count = {}
        for i in self.data:
            count[i] = self.data.count(i)
        print(count)
        l = []
        maxi = max(count.values())
        for i in count:
            if count[i] == maxi:
                l.append(i)
        return min(l)

from random import randint        
obj = Statistics([randint(1,10) for var in range(20)])
print("Mode : ",obj.mode())
print("Median : ",obj.median())
print("Mean : ",obj.mean())
