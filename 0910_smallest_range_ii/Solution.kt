// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

class Solution {
    fun smallestRangeII(nums: IntArray, k: Int): Int {
        nums.sort()
        var ans = nums[nums.size - 1] - nums[0]
        for (i in 0 until nums.size - 1) {
            val lo = minOf(nums[0] + k, nums[i + 1] - k)
            val hi = maxOf(nums[nums.size - 1] - k, nums[i] + k)
            ans = minOf(ans, hi - lo)
        }
        return ans
    }
}
