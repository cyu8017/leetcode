// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution {
    fun maxTotalValue(nums: IntArray, k: Int): Long {
        var mn = nums[0]
        var mx = nums[0]
        for (x in nums) {
            mn = minOf(mn, x)
            mx = maxOf(mx, x)
        }
        return 1L * k * (mx - mn)
    }
}
