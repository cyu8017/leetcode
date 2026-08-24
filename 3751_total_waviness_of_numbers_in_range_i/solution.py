# LeetCode 3751 - Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def F(x: int) -> int:
            nums = []
            while x > 0:
                nums.append(x % 10)
                x //= 10
            m = len(nums)
            if m < 3:
                return 0
            s = 0
            for i in range(1, m - 1):
                if ((nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or
                        (nums[i] < nums[i - 1] and nums[i] < nums[i + 1])):
                    s += 1
            return s

        ans = 0
        for x in range(num1, num2 + 1):
            ans += F(x)
        return ans
