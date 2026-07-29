// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution {
    fun sumOfDigits(nums: IntArray): Int {
        var n = nums[0]
        for (x in nums) if (x < n) n = x
        var digitSum = 0
        while (n > 0) {
            digitSum += n % 10
            n /= 10
        }
        return if (digitSum % 2 == 0) 1 else 0
    }
}
