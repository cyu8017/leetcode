class ProductOfNumbers:
    def __init__(self):
        self.p = [1]
    def add(self, num):
        if num == 0: self.p = [1]
        else: self.p.append(self.p[-1] * num)
    def getProduct(self, k):
        return 0 if k >= len(self.p) else self.p[-1] // self.p[-1-k]
