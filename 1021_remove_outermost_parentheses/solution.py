# LeetCode 1021 - Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0
        for ch in s:
            if ch == "(":
                if depth:
                    ans.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth:
                    ans.append(ch)
        return "".join(ans)
