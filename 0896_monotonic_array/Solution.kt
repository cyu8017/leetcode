// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

class Solution {
    fun isMonotonic(nums: IntArray): Boolean {
        var inc = true
        var dec = true
        for (i in 1 until nums.size) {
            if (nums[i] < nums[i - 1]) inc = false
            if (nums[i] > nums[i - 1]) dec = false
        }
        return inc || dec
    }
}
