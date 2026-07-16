# LeetCode 0969 - Pancake Sorting
# https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        a = arr[:]
        ans: list[int] = []
        for size in range(len(a), 1, -1):
            i = a.index(size)
            if i == size - 1:
                continue
            if i:
                ans.append(i + 1)
                a[: i + 1] = a[: i + 1][::-1]
            ans.append(size)
            a[:size] = a[:size][::-1]
        return ans
