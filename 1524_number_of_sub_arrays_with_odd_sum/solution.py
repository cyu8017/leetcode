# LeetCode 1524

class Solution:
    def numOfSubarrays(self, arr):
        counts = [1, 0]
        parity = answer = 0
        for value in arr:
            parity ^= value & 1
            answer += counts[parity ^ 1]
            counts[parity] += 1
        return answer % 1000000007
