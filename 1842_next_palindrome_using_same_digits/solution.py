# LeetCode 1842 - Next Palindrome Using Same Digits
# https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution:
    def nextPalindrome(self, num: str) -> str:
        nums = list(num)

        if not self._next_permutation(nums):
            return ""

        n = len(nums)
        for i in range(n // 2):
            nums[n - i - 1] = nums[i]
        return "".join(nums)

    def _next_permutation(self, nums: list[str]) -> bool:
        n = len(nums) // 2
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return False

        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 : n] = nums[i + 1 : n][::-1]
        return True
