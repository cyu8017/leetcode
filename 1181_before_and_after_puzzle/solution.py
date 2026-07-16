# LeetCode 1181 - Before and After Puzzle
# https://leetcode.com/problems/before-and-after-puzzle/

class Solution:
    def beforeAndAfterPuzzles(self, phrases: list[str]) -> list[str]:
        split = [p.split() for p in phrases]
        result: set[str] = set()
        for i in range(len(split)):
            for j in range(len(split)):
                if i == j:
                    continue
                if split[i][-1] == split[j][0]:
                    result.add(" ".join(split[i] + split[j][1:]))
        return sorted(result)
