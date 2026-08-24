// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution {
    private val NEG: Long = -1e18
    private var nums: IntArray? = null
    private var memo: Array<LongArray>? = null
    private var n: Int = 0

    fun maximumTotalCost(nums: IntArray): Long {
        this.nums = nums
        n = nums.size
        memo = Array(n) { LongArray(2) }
        for (i in 0 until n) {
            memo[i][0] = memo[i][1] = NEG
        }
        return dfs(0, 0)
    }

    private fun dfs(i: Int, j: Int): Long {
        if (i >= n) {
            return 0
        }
        if (memo[i][j] != NEG) {
            return memo[i][j]
        }
        var res = nums[i] + dfs(i + 1, 1)
        if (j > 0) {
            res = maxOf(res, -nums[i] + dfs(i + 1, 0))
        }
        return memo[i][j] = res
    }
}
