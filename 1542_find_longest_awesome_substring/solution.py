# LeetCode 1542

class Solution:
    def longestAwesome(self, s):
        first = {0: -1}
        mask = answer = 0
        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)
            if mask in first:
                answer = max(answer, i - first[mask])
            else:
                first[mask] = i
            for bit in range(10):
                candidate = mask ^ (1 << bit)
                if candidate in first:
                    answer = max(answer, i - first[candidate])
        return answer
