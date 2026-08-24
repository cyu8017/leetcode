// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution {
    fun numSubarrayBoundedMax(nums: IntArray, left: Int, right: Int): Int {
        return countAtMost(nums, right) - countAtMost(nums, left - 1)
    }

    private fun countAtMost(nums: IntArray, bound: Int): Int {
        var ans = 0
        var cur = 0
        for (num in nums) {
            if (num <= bound) {
                cur++
                ans += cur
            } else {
                cur = 0
            }
        }
        return ans
    }
}
