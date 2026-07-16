class Solution:
    def reformat(self, s):
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(digits) >= len(letters):
            letters, digits = digits, letters
        answer = []
        for i, char in enumerate(letters):
            answer.append(char)
            if i < len(digits):
                answer.append(digits[i])
        return "".join(answer)
