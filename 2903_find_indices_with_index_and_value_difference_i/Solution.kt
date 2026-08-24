// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/


class Solution {
    fun findIndices(nums: IntArray, indexDifference: Int, valueDifference: Int): IntArray {
        val n = nums.size
        for (i in 0 until n) {
            for (j in i until n) {
                val di = kotlin.math.abs(j - i)
                val dv = kotlin.math.abs(nums[i] - nums[j])
                if (di >= indexDifference && dv >= valueDifference) return intArrayOf(i, j)
            }
        }
        return intArrayOf(-1, -1)
    }
}
