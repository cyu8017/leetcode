class Solution:
    def maxPower(self, s):
        answer = run = 1
        for i in range(1, len(s)):
            run = run + 1 if s[i] == s[i - 1] else 1
            answer = max(answer, run)
        return answer
