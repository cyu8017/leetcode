# LeetCode 2281 - Sum of Total Strength of Wizards
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/

from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 1000000007
        n = len(strength)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        pref = [0] * (n + 1)
        pref_pref = [0] * (n + 2)
        for i in range(n):
            pref[i + 1] = (pref[i] + strength[i]) % mod
        for i in range(n + 1):
            pref_pref[i + 1] = (pref_pref[i] + pref[i]) % mod
        ans = 0
        for i in range(n):
            l, r = left[i] + 1, right[i] - 1
            left_sum = (pref_pref[i + 1] - pref_pref[l] + mod) % mod
            right_sum = (pref_pref[r + 2] - pref_pref[i + 1] + mod) % mod
            left_cnt = i - l + 1
            right_cnt = r - i + 1
            contrib = (right_cnt * left_sum % mod - left_cnt * right_sum % mod + mod) % mod
            ans = (ans + contrib * strength[i] % mod) % mod
        return ans
