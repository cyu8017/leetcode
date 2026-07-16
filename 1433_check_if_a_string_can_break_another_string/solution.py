class Solution:
    def checkIfCanBreak(self, s1, s2):
        a, b = sorted(s1), sorted(s2)
        return all(x >= y for x, y in zip(a, b)) or all(x <= y for x, y in zip(a, b))
