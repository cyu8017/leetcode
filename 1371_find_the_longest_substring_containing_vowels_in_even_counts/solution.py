class Solution:
    def findTheLongestSubstring(self, s):
        first={0:-1}; mask=ans=0
        for i,c in enumerate(s):
            if c in 'aeiou':mask^=1<<'aeiou'.index(c)
            if mask in first:ans=max(ans,i-first[mask])
            else:first[mask]=i
        return ans
