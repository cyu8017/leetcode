class Solution:
    def maximumScore(self, a, b, c):
        stones = sorted([a, b, c], reverse=True)
        score = 0
        while stones[0] > 0 and stones[1] > 0:
            stones[0] -= 1
            stones[1] -= 1
            score += 1
            stones.sort(reverse=True)
        return score
