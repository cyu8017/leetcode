# LeetCode 1343 - Number Of Sub Arrays Of Size K And Average Greater Than Or Equal To Threshold

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        answer = int(window >= k * threshold)
        for i in range(k, len(arr)):
            window += arr[i] - arr[i-k]
            answer += window >= k * threshold
        return answer
