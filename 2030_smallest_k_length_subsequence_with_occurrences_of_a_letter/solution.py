# LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        remain_letter = sum(1 for c in s if c == letter)
        stack = []
        in_stack_letter = 0
        for i, ch in enumerate(s):
            while stack and ch < stack[-1] and len(stack) + n - i > k:
                top = stack[-1]
                if top == letter:
                    if in_stack_letter + remain_letter - 1 < repetition:
                        break
                    in_stack_letter -= 1
                stack.pop()
            if len(stack) < k:
                if ch == letter:
                    stack.append(ch)
                    in_stack_letter += 1
                elif k - len(stack) > repetition - in_stack_letter:
                    stack.append(ch)
            if ch == letter:
                remain_letter -= 1
        return "".join(stack)
