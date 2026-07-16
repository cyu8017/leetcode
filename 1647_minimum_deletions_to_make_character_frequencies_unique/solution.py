class Solution:
    def minDeletions(self, s):
        from collections import Counter
        used=set(); ans=0
        for x in Counter(s).values():
            while x and x in used: x-=1; ans+=1
            used.add(x)
        return ans
