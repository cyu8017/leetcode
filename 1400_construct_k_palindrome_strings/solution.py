from collections import Counter
class Solution:
    def canConstruct(self, s, k):
        return sum(v%2 for v in Counter(s).values())<=k<=len(s)
