# LeetCode 3609 - Minimum Moves to Reach Target in Grid
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/


class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        ans = 0
        while tx > sx or ty > sy:
            if tx < sx or ty < sy:
                return -1
            if tx == ty:
                return -1
            if tx > ty:
                if ty > sy:
                    if tx >= 2 * ty:
                        if tx % 2 != 0:
                            return -1
                        tx //= 2
                    else:
                        tx -= ty
                    ans += 1
                else:
                    if ty != sy:
                        return -1
                    while tx > sx:
                        if tx >= 2 * ty:
                            if tx % 2 != 0:
                                return -1
                            tx //= 2
                        else:
                            tx -= ty
                        ans += 1
                        if tx < sx:
                            return -1
            else:
                if tx > sx:
                    if ty >= 2 * tx:
                        if ty % 2 != 0:
                            return -1
                        ty //= 2
                    else:
                        ty -= tx
                    ans += 1
                else:
                    if tx != sx:
                        return -1
                    while ty > sy:
                        if ty >= 2 * tx:
                            if ty % 2 != 0:
                                return -1
                            ty //= 2
                        else:
                            ty -= tx
                        ans += 1
                        if ty < sy:
                            return -1
        return ans if tx == sx and ty == sy else -1
