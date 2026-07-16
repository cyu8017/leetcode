class Solution:
    def maxHeight(self, cuboids):
        a=[sorted(x) for x in cuboids];a.sort();n=len(a);dp=[0]*n
        for i in range(n):
            dp[i]=a[i][2]
            for j in range(i):
                if all(a[j][d]<=a[i][d] for d in range(3)):dp[i]=max(dp[i],dp[j]+a[i][2])
        return max(dp)
