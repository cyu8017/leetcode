class Solution:
    def luckyNumbers(self, matrix):
        mins={min(r) for r in matrix}; maxs={max(c) for c in zip(*matrix)}
        return list(mins&maxs)
