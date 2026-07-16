class Solution:
    def getSmallestString(self, n, k):
        a=["a"]*n; k-=n
        for i in range(n-1,-1,-1):
            d=min(25,k);a[i]=chr(97+d);k-=d
        return "".join(a)
