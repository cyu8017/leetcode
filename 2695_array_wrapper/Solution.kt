// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper(private val nums: IntArray) {
    fun valueOf(): Int {
        var s = 0
        for (x in nums) s += x
        return s
    }

    override fun toString(): String {
        val sb = StringBuilder()
        sb.append('[')
        for (i in nums.indices) {
            if (i > 0) sb.append(',')
            sb.append(nums[i])
        }
        sb.append(']')
        return sb.toString()
    }
}

class Solution {
    fun arrayWrapperCreate(nums: IntArray): ArrayWrapper = ArrayWrapper(nums)
}
