from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        frequency, odd, answer = defaultdict(int, {0: 1}), 0, 0
        for x in nums:
            odd += x & 1
            answer += frequency[odd - k]
            frequency[odd] += 1
        return answer
