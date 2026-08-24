// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution {
    fun maxStrength(nums: IntArray): Long {
        nums.sort()
        val n = nums.size
        if (n == 1) return nums[0].toLong()
        var prod = 1L
        var used = false
        var i = 0
        while (i + 1 < n && nums[i] < 0 && nums[i + 1] < 0) {
            prod *= 1L * nums[i] * nums[i + 1]
            used = true
            i += 2
        }
        val negLeft = i < n && nums[i] < 0
        while (i < n) {
            if (nums[i] > 0) {
                prod *= nums[i]
                used = true
            }
            i++
        }
        if (!used) {
            if (negLeft) {
                for (x in nums) if (x == 0) return 0
                return nums[n - 1].toLong()
            }
            return 0
        }
        return prod
    }
}
