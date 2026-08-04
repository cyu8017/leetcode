// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution {
    fun getMaxLen(nums: IntArray): Int {
        var positive = 0
        var negative = 0
        var answer = 0
        for (x in nums) {
            when {
                x == 0 -> {
                    positive = 0
                    negative = 0
                }
                x > 0 -> {
                    positive++
                    negative = if (negative == 0) 0 else negative + 1
                }
                else -> {
                    val nextPositive = if (negative == 0) 0 else negative + 1
                    negative = positive + 1
                    positive = nextPositive
                }
            }
            answer = maxOf(answer, positive)
        }
        return answer
    }
}
