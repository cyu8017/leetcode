class Solution:
    def countSubstrings(self, s, t):
        ans=0
        for i in range(len(s)):
            for j in range(len(t)):
                diff=0
                for k in range(min(len(s)-i,len(t)-j)):
                    diff += s[i+k] != t[j+k]
                    if diff==1: ans+=1
                    elif diff>1: break
        return ans
