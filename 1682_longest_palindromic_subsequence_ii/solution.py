class Solution:
    def longestPalindromeSubseq(self, s):
        n=len(s);dp=[[[0]*26 for _ in range(n)] for _ in range(n)]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                for c in range(26):dp[i][j][c]=max(dp[i+1][j][c],dp[i][j-1][c])
                if s[i]==s[j]:
                    c=ord(s[i])-97
                    inner=0 if length==2 else max((dp[i+1][j-1][x] for x in range(26) if x!=c),default=0)
                    dp[i][j][c]=max(dp[i][j][c],inner+2)
        return max(dp[0][n-1])
