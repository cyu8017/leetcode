# LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = [0] * len(seq)
        for i, ch in enumerate(seq):
            if ch == "(":
                ans[i] = depth % 2
                depth += 1
            else:
                depth -= 1
                ans[i] = depth % 2
        return ans
