class Solution:
    def minSwaps(self, s: str) -> int:
        bal = 0
        mx = 0
        for ch in s:
            if ch == "[":
                bal += 1
            else:
                bal -= 1
            mx = min(mx, bal)
        return (-mx + 1) // 2
