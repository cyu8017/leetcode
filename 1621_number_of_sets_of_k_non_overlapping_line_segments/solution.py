class Solution:
    def numberOfSets(self, n, k):
        import math
        return math.comb(n + k - 1, 2 * k) % 1000000007
