// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

class Solution {
    fun find132pattern(nums: IntArray): Boolean {
        val stack = ArrayDeque<Int>()
        var third = Int.MIN_VALUE
        for (value in nums.reversed()) {
            if (value < third) {
                return true
            }
            while (stack.isNotEmpty() && value > stack.last()) {
                third = stack.removeLast()
            }
            stack.addLast(value)
        }
        return false
    }
}
