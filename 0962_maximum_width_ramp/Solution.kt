// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

class Solution {
    fun maxWidthRamp(nums: IntArray): Int {
        var stack = mutableListOf()
        for (i in 0 until nums.size) {
            if (stack.isEmpty() || nums[stack[stack.size - 1]] > nums[i]) stack.add(i)
        }
        var ans = 0
        for (j in nums.size - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack[stack.size - 1]] <= nums[j]) {
                ans = maxOf(ans, j - stack[stack.size - 1])
                stack.removeAt(stack.size - 1)
            }
        }
        return ans
    }
}
