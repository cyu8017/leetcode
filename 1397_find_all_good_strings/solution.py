from functools import lru_cache
class Solution:
    def findGoodStrings(self, n, s1, s2, evil):
        mod=1_000_000_007;m=len(evil);pi=[0]*m
        for i in range(1,m):
            j=pi[i-1]
            while j and evil[i]!=evil[j]:j=pi[j-1]
            if evil[i]==evil[j]:j+=1
            pi[i]=j
        trans=[[0]*26 for _ in range(m)]
        for j in range(m):
            for x in range(26):
                c=chr(97+x);k=j
                while k and evil[k]!=c:k=pi[k-1]
                if evil[k]==c:k+=1
                trans[j][x]=k
        @lru_cache(None)
        def dp(i,j,lo,hi):
            if j==m:return 0
            if i==n:return 1
            a=ord(s1[i])-97 if lo else 0;b=ord(s2[i])-97 if hi else 25;ans=0
            for x in range(a,b+1):
                ans+=dp(i+1,trans[j][x],lo and x==a,hi and x==b)
            return ans%mod
        return dp(0,0,True,True)
