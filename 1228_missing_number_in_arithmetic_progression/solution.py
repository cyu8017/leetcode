class Solution:
    def missingNumber(self, arr: list[int]) -> int:
        difference = (arr[-1] - arr[0]) // len(arr)
        for i in range(1, len(arr)):
            expected = arr[0] + i * difference
            if arr[i] != expected: return expected
        return arr[0]
