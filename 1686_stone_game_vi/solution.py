class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        order=sorted(range(len(aliceValues)),key=lambda i:aliceValues[i]+bobValues[i],reverse=True)
        score=sum(aliceValues[i] if t%2==0 else -bobValues[i] for t,i in enumerate(order))
        return (score>0)-(score<0)
