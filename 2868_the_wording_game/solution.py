# LeetCode 2868 - The Wording Game
# https://leetcode.com/problems/the-wording-game/

from typing import List


class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:
        def closely_greater(w: str, z: str) -> bool:
            return w > z and (w[0] == z[0] or ord(w[0]) == ord(z[0]) + 1)

        i, j = 1, 0
        last = a[0]
        alice = False
        while True:
            if alice:
                while i < len(a) and not closely_greater(a[i], last):
                    i += 1
                if i == len(a):
                    return False
                last = a[i]
                i += 1
            else:
                while j < len(b) and not closely_greater(b[j], last):
                    j += 1
                if j == len(b):
                    return True
                last = b[j]
                j += 1
            alice = not alice
