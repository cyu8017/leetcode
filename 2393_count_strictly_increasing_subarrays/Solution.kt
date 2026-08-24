// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

class Solution {
    fun countSubarrays(nums: IntArray): Long {
        var ans = 0L
        var len = 0L
        for (i in nums.indices) {
            if (i > 0 && nums[i] > nums[i - 1]) len++
            else len = 1
            ans += len
        }
        return ans
    }
}
