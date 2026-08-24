// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

class Solution {
    fun minMaxSubarraySum(nums: IntArray, k: Int): Long {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var mn = nums[i]
            var mx = nums[i]
            for (j in i until n && j - i + 1 <= k) {
                if (nums[j] < mn) mn = nums[j]
                if (nums[j] > mx) mx = nums[j]
                ans += mn + mx
            }
        }
        return ans
    }
}
