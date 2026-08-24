// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

class Solution {
    fun maxSumAfterOperation(nums: IntArray): Int {
        var noSquare = 0L
        var oneSquare = 0L
        var best = Long.MIN_VALUE
        for (value in nums) {
            val v = value.toLong()
            oneSquare = maxOf(oneSquare + v, noSquare + v * v, v * v)
            noSquare = maxOf(noSquare + v, v)
            best = maxOf(best, oneSquare)
        }
        return best.toInt()
    }
}
