class Solution:
    def maxSizeSlices(self, slices):
        k=len(slices)//3
        def line(a):
            dp=[[0]*(k+1) for _ in range(len(a)+2)]
            for i,x in enumerate(a,2):
                for j in range(1,k+1):dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+x)
            return dp[-1][k]
        return max(line(slices[:-1]),line(slices[1:]))
