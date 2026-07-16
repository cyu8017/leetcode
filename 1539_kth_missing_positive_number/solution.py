# LeetCode 1539

class Solution:
    def findKthPositive(self, arr, k):
        left, right = 0, len(arr)
        while left < right:
            middle = (left + right) // 2
            if arr[middle] - middle - 1 < k:
                left = middle + 1
            else:
                right = middle
        return left + k
