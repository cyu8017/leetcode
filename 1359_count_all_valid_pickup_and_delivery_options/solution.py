class Solution:
    def countOrders(self, n):
        ans=1
        for i in range(1,n+1): ans=ans*i*(2*i-1)%1_000_000_007
        return ans
