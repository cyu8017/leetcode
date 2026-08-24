// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

class Solution {
    fun maximumMedianSum(nums: IntArray): Long {
        nums.sort()
        var n = nums.size
        var ans = 0
        run {
            var i = n / 3
            while (i < n) {
                ans += nums[i]
                i += 2
            }
        }
        return ans
    }
}
