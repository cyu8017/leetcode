class Solution:
    def stringShift(self, s, shift):
        offset = 0
        for direction, amount in shift:
            offset += amount if direction else -amount
        offset %= len(s)
        return s[-offset:] + s[:-offset] if offset else s
