class Solution:
    def areAlmostEqual(self, s1, s2):
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])
