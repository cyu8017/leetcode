# LeetCode 0301 - Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(text: str) -> bool:
            balance = 0
            for char in text:
                if char == "(":
                    balance += 1
                elif char == ")":
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        result: set[str] = set()
        queue = [s]
        visited = {s}
        found = False
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)
                if is_valid(current):
                    result.add(current)
                    found = True
                if found:
                    continue
                for index in range(len(current)):
                    if current[index] not in "()":
                        continue
                    nxt = current[:index] + current[index + 1 :]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        return list(result)
