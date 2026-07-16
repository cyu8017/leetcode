# LeetCode 0845 - Longest Mountain in Array
# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        ans = i = 0
        while i < n:
            j = i
            if j + 1 < n and arr[j] < arr[j + 1]:
                while j + 1 < n and arr[j] < arr[j + 1]:
                    j += 1
                if j + 1 < n and arr[j] > arr[j + 1]:
                    while j + 1 < n and arr[j] > arr[j + 1]:
                        j += 1
                    ans = max(ans, j - i + 1)
                    i = j
                    continue
            i += 1
        return ans
