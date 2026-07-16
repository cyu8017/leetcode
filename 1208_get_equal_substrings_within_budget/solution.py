class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = answer = 0
        for right, (a, b) in enumerate(zip(s, t)):
            cost += abs(ord(a) - ord(b))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            answer = max(answer, right - left + 1)
        return answer
