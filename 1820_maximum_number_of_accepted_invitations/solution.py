# LeetCode 1820 - Maximum Number of Accepted Invitations
# https://leetcode.com/problems/maximum-number-of-accepted-invitations/

from typing import List


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        boys = len(grid)
        girls = len(grid[0])
        match_girl = [-1] * girls

        def dfs(boy: int, seen: list[bool]) -> bool:
            for girl in range(girls):
                if grid[boy][girl] and not seen[girl]:
                    seen[girl] = True
                    if match_girl[girl] == -1 or dfs(match_girl[girl], seen):
                        match_girl[girl] = boy
                        return True
            return False

        ans = 0
        for boy in range(boys):
            if dfs(boy, [False] * girls):
                ans += 1
        return ans
