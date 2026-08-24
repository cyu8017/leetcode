// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

class Solution {
    fun maxSum(nums: IntArray, k: Int, mul: Int): Long {
        nums.sort()
        var n = nums.size
        var ans = 0
        for (i in n - 1 downTo n - k) {
            var m = maxOf(1, mul)
            ans += nums[i] * m
            mul--
        }
        return ans
    }
}
