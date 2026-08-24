# LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for i in range(k):
            if blocks[i] == "W":
                white += 1
        ans = white
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                white += 1
            if blocks[i - k] == "W":
                white -= 1
            ans = min(ans, white)
        return ans
