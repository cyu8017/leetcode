from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0
        answer, left = right, 0
        while left == 0 or (left < n and arr[left - 1] <= arr[left]):
            while right < n and arr[right] < arr[left]:
                right += 1
            answer = min(answer, right - left - 1)
            left += 1
            if left >= n:
                break
        return answer
