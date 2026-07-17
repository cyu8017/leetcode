# LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(arr: list[str]) -> None:
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i < 0:
                arr.reverse()
                return
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1 :] = reversed(arr[i + 1 :])

        target = list(num)
        for _ in range(k):
            next_permutation(target)

        source = list(num)
        swaps = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            j = i
            while source[j] != target[i]:
                j += 1
            while j > i:
                source[j], source[j - 1] = source[j - 1], source[j]
                swaps += 1
                j -= 1
        return swaps
