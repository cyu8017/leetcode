class CustomStack:
    def __init__(self, maxSize):self.maxSize=maxSize;self.a=[]
    def push(self, x):
        if len(self.a)<self.maxSize:self.a.append(x)
    def pop(self):return self.a.pop() if self.a else -1
    def increment(self, k, val):
        for i in range(min(k,len(self.a))):self.a[i]+=val
