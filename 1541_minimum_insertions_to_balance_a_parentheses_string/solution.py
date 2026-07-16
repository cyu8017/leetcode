# LeetCode 1541

class Solution:
    def minInsertions(self, s):
        insertions = needed = i = 0
        while i < len(s):
            if s[i] == "(":
                needed += 2
                if needed & 1:
                    insertions += 1
                    needed -= 1
            else:
                needed -= 1
                if needed < 0:
                    insertions += 1
                    needed = 1
            i += 1
        return insertions + needed
