from collections import Counter
class Solution:
    def findLucky(self, arr):
        return max((x for x,c in Counter(arr).items() if x==c),default=-1)
