# LeetCode 0975 - Odd Even Jump
# https://leetcode.com/problems/odd-even-jump/

class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        n = len(arr)
        next_higher = [0] * n
        next_lower = [0] * n
        stack: list[int] = []
        for a, i in sorted((a, i) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        stack.clear()
        for a, i in sorted((-a, i) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for i in range(n - 2, -1, -1):
            if next_higher[i]:
                odd[i] = even[next_higher[i]]
            if next_lower[i]:
                even[i] = odd[next_lower[i]]
        return sum(odd)
