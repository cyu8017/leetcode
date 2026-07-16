# LeetCode 0957 - Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/

class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        seen: dict[tuple[int, ...], int] = {}
        state = tuple(cells)
        while n:
            if state in seen:
                cycle = seen[state] - n
                n %= cycle
                if n == 0:
                    break
            seen[state] = n
            nxt = [0] + [int(state[i - 1] == state[i + 1]) for i in range(1, 7)] + [0]
            state = tuple(nxt)
            n -= 1
        return list(state)
