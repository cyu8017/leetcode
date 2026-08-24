// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

class Solution {
    fun upperBound(nums: IntArray, target: Int): Int {
        var lo = 0
        var hi = nums.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (nums[mid] <= target) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
