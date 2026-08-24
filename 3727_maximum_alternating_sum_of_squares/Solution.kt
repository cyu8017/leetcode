// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution {
    fun maxAlternatingSum(nums: IntArray): Long {
        for (i in 0 until nums.size) { nums[i] *= nums[i] }
        nums.sort()
        var m = nums.size / 2
        var ans = 0
        for (i in 0 until m) { ans -= nums[i] }
        for (i in m until nums.size) { ans += nums[i] }
        return ans
    }
}
