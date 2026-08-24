// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

class Solution {
    fun rangeSum(nums: IntArray): Int {
        val mod = 1000000007
        var n = nums.size
        var ans = 0
        var i = 0
        while (i < n) {
            var j = i
            while (j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1)) j++
            for (L in i ..j) {
                var s = 0
                for (R in L ..j) {
                    s += nums[R]
                    ans = (ans + s) % mod
                }
            }
            i = j + 1
        }
        return ans
    }
}
