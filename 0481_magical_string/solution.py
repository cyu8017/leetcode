# LeetCode 0481 - Magical String
# https://leetcode.com/problems/magical-string/

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        seq = [1, 2, 2]
        i = 2
        while len(seq) < n:
            if seq[i] == 1:
                seq.append(1 if seq[-1] == 2 else 2)
            else:
                seq.extend([1 if seq[-1] == 2 else 2] * 2)
            i += 1
        return seq[:n].count(1)
