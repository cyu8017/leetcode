from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        count, frequencies = Counter(), Counter()
        answer = 0
        for i, x in enumerate(nums, 1):
            old = count[x]
            if old: frequencies[old] -= 1
            count[x] += 1
            frequencies[old + 1] += 1
            high = max(frequencies)
            if high == 1 or frequencies[high] * high + 1 == i or frequencies[high] == 1 and frequencies[high - 1] * (high - 1) + high == i:
                answer = i
        return answer
