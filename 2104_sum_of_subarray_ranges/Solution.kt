// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution {
    fun subArrayRanges(nums: IntArray): Long {
        var n: Int = nums.size
        var ans: Long = 0
        for (i in 0 until n) {
            var mn: Int = nums[i], mx = nums[i]
            for (j in i until n) {
                mn = minOf(mn, nums[j])
                mx = maxOf(mx, nums[j])
                ans += mx - mn
            }
        }
        return ans
    }
}
