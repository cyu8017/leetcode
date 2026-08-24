// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

class Solution {
    fun isArraySpecial(nums: IntArray, queries: Array<IntArray>): BooleanArray {
        val n = nums.size
        val d = IntArray(n) { it }
        for (i in 1 until n) {
            if (nums[i] % 2 != nums[i - 1] % 2) d[i] = d[i - 1]
        }
        return BooleanArray(queries.size) { i -> d[queries[i][1]] <= queries[i][0] }
    }
}
