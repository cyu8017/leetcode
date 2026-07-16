class Solution:
    def secondHighest(self, s):
        digits = sorted({int(ch) for ch in s if ch.isdigit()})
        return digits[-2] if len(digits) > 1 else -1
