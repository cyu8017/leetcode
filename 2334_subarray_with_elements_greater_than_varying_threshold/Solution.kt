// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

class Solution {
    fun validSubarraySize(nums: IntArray, threshold: Int): Int {
        val n = nums.size
        val left = IntArray(n)
        val right = IntArray(n)
        val stack = ArrayList<Int>()
        for (i in 0 until n) {
            while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) stack.removeAt(stack.lastIndex)
            left[i] = if (stack.isEmpty()) -1 else stack.last()
            stack.add(i)
        }
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (stack.isNotEmpty() && nums[stack.last()] >= nums[i]) stack.removeAt(stack.lastIndex)
            right[i] = if (stack.isEmpty()) n else stack.last()
            stack.add(i)
        }
        for (i in 0 until n) {
            val k = right[i] - left[i] - 1
            if (nums[i] > threshold / k) return k
        }
        return -1
    }
}
