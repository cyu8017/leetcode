// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

class Solution {
    fun nextGreaterElements(nums: IntArray): IntArray {
        val length = nums.size
        val result = IntArray(length) { -1 }
        val stack = ArrayDeque<Int>()
        for (index in 0 until length * 2) {
            val value = nums[index % length]
            while (stack.isNotEmpty() && nums[stack.last()] < value) {
                result[stack.removeLast()] = value
            }
            if (index < length) {
                stack.addLast(index)
            }
        }
        return result
    }
}
