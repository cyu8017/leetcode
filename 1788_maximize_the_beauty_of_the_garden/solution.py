class Solution:
    def maximumBeauty(self, flowers):
        best = float("-inf")
        left_best = {}
        for cur in flowers:
            if cur in left_best:
                best = max(best, left_best[cur] + cur)
            for val in list(left_best.keys()):
                if val > cur:
                    left_best[val] = max(left_best[val], left_best[val] + cur)
                else:
                    left_best.pop(val)
            left_best[cur] = max(left_best.get(cur, float("-inf")), cur)
        return best
