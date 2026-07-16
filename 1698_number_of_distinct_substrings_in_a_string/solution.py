class Solution:
    def countDistinct(self, s):
        root={};ans=0
        for i in range(len(s)):
            node=root
            for c in s[i:]:
                if c not in node:node[c]={};ans+=1
                node=node[c]
        return ans
