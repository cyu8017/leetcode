class Solution:
    def numberOfSubstrings(self, s):
        last=[-1]*3; ans=0
        for i,c in enumerate(s):
            last[ord(c)-97]=i; ans+=min(last)+1
        return ans
