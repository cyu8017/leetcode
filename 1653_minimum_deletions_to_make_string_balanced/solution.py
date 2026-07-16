class Solution:
    def minimumDeletions(self, s):
        b=ans=0
        for c in s:
            if c=="b": b+=1
            else: ans=min(ans+1,b)
        return ans
