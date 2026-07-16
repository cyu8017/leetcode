# LeetCode 1320 - Minimum Distance To Type A Word Using Two Fingers

class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(a, b):
            if a == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        letters = [ord(ch) - 65 for ch in word]
        dp = {26: 0}
        previous = letters[0]
        for current in letters[1:]:
            nxt = {}
            for free, cost in dp.items():
                nxt[free] = min(nxt.get(free, 10**9), cost + distance(previous, current))
                nxt[previous] = min(nxt.get(previous, 10**9), cost + distance(free, current))
            dp, previous = nxt, current
        return min(dp.values())
