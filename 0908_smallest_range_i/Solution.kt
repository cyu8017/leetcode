// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

class Solution {
    fun smallestRangeI(nums: IntArray, k: Int): Int {
        var mn = nums[0]
        var mx = nums[0]
        for (x in nums) {
            mn = minOf(mn, x)
            mx = maxOf(mx, x)
        }
        return maxOf(0, mx - mn - 2 * k)
    }
}
