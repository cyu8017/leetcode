# LeetCode 0473 - Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square/


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        if not matchsticks:
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)

        def dfs(index: int, sides: list[int]) -> bool:
            if index == len(matchsticks):
                return sides[0] == side and len(set(sides)) == 1
            length = matchsticks[index]
            for side_index in range(4):
                if sides[side_index] + length > side:
                    continue
                if side_index > 0 and sides[side_index] == sides[side_index - 1]:
                    continue
                sides[side_index] += length
                if dfs(index + 1, sides):
                    return True
                sides[side_index] -= length
            return False

        return dfs(0, [0, 0, 0, 0])
