// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution {
    fun maxArrayValue(nums: IntArray): Long {
        var n = nums.size
        var cur = nums[n - 1]
        var ans = cur
        for (i in n - 2 downTo 0) {
            if (nums[i] <= cur) cur += nums[i]
            else cur = nums[i]
            ans = maxOf(ans, cur)
        }
        return ans
    }
}
