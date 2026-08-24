// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution {
    fun minimumPrefixLength(nums: IntArray): Int {
        var i = nums.size - 1
        while (i > 0) {
            if (nums[i - 1] >= nums[i]) return i
            i = i - 1
        }
        return 0
    }
}
