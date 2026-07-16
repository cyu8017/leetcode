class Cashier:
    def __init__(self, n, discount, products, prices):
        self.n=n; self.discount=discount; self.price=dict(zip(products,prices)); self.count=0
    def getBill(self, product, amount):
        self.count+=1
        total=sum(self.price[p]*a for p,a in zip(product,amount))
        return total*(100-self.discount)/100 if self.count%self.n==0 else float(total)
