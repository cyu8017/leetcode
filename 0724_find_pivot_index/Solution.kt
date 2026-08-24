// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

class Solution {
    fun pivotIndex(nums: IntArray): Int {
        var total = 0
        for (x in nums) { total += x }
        var left = 0
        for (i in 0 until nums.size) {
            if (left == total - left - nums[i]) return i
            left += nums[i]
        }
        return -1
    }
}
