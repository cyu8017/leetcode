from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        count, limit = Counter(s), len(s) // 4
        n = len(s)
        left, answer = 0, n
        for right, ch in enumerate(s):
            count[ch] -= 1
            while left < n and all(count[c] <= limit for c in 'QWER'):
                answer = min(answer, right - left + 1)
                count[s[left]] += 1
                left += 1
        return answer
