class Solution:
    def numWays(self, words, target):
        MOD=1000000007; m=len(words[0]); dp=[1]+[0]*len(target)
        for j in range(m):
            count=[0]*26
            for word in words: count[ord(word[j])-97]+=1
            for i in range(min(j+1,len(target)),0,-1):
                dp[i]=(dp[i]+dp[i-1]*count[ord(target[i-1])-97])%MOD
        return dp[-1]
