class Solution:
    def maxScore(self, s):
        ones = s.count("1")
        left_zeros = answer = 0
        for char in s[:-1]:
            if char == "0":
                left_zeros += 1
            else:
                ones -= 1
            answer = max(answer, left_zeros + ones)
        return answer
