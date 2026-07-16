// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution {
    fun findMaxConsecutiveOnes(nums: IntArray): Int {
        var left = 0
        var best = 0
        var zeros = 0
        for (right in nums.indices) {
            if (nums[right] == 0) {
                zeros += 1
            }
            while (zeros > 1) {
                if (nums[left] == 0) {
                    zeros -= 1
                }
                left += 1
            }
            best = maxOf(best, right - left + 1)
        }
        return best
    }
}
