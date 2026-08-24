// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

class Solution {
    fun countNonDecreasingSubarrays(nums: IntArray, k: Int): Long {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var cost = 0
            var maxV = nums[i]
            for (j in i until n) {
                if (nums[j] >= maxV) maxV = nums[j]
                else cost += maxV - nums[j]
                if (cost > k) break
                ans = ans + 1
            }
        }
        return ans
    }
}
