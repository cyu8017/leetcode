from collections import Counter
class Solution:
    def countLargestGroup(self, n):
        c=Counter(sum(map(int,str(x))) for x in range(1,n+1));m=max(c.values())
        return sum(v==m for v in c.values())
