class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[0]*(len(t)+1); dp[0]=1
        for char in s:
            for index in range(len(t)-1, -1, -1):
                if char == t[index]: dp[index+1] += dp[index]
        return dp[-1]
