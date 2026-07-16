# LeetCode 1525

class Solution:
    def numSplits(self, s):
        from collections import Counter
        right = Counter(s)
        left = set()
        answer = 0
        for ch in s[:-1]:
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                del right[ch]
            answer += len(left) == len(right)
        return answer
