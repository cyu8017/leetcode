class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = answer = 0
        for ch in s:
            balance += 1 if ch == 'L' else -1
            answer += balance == 0
        return answer
