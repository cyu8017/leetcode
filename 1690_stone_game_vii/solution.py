class Solution:
    def stoneGameVII(self, stones):
        n=len(stones);pre=[0]
        for x in stones:pre.append(pre[-1]+x)
        dp=[[0]*n for _ in range(n)]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                dp[i][j]=max(pre[j+1]-pre[i+1]-dp[i+1][j],pre[j]-pre[i]-dp[i][j-1])
        return dp[0][n-1]
