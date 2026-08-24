// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution {
    fun zeroFilledSubarray(nums: IntArray): Long {
        var ans = 0L
        var streak = 0L
        for (x in nums) {
            if (x == 0) {
                streak++
                ans += streak
            } else streak = 0
        }
        return ans
    }
}
