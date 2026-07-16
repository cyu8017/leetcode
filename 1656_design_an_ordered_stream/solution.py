class OrderedStream:
    def __init__(self, n):
        self.a=[None]*(n+1); self.p=1
    def insert(self, idKey, value):
        self.a[idKey]=value; out=[]
        while self.p<len(self.a) and self.a[self.p] is not None:
            out.append(self.a[self.p]); self.p+=1
        return out
