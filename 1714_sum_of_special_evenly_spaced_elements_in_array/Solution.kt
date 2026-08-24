// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

class Solution {
    fun solve(nums: IntArray, queries: Array<IntArray>): IntArray {
        val mod = 1_000_000_007L
        val n = nums.size
        val block = Math.sqrt(n.toDouble()).toInt() + 1
        val dp = Array(block) { IntArray(n) }
        for (step in 1 until block) {
            for (i in n - 1 downTo 0) {
                val next = if (i + step < n) dp[step][i + step].toLong() else 0L
                dp[step][i] = ((nums[i] + next) % mod).toInt()
            }
        }
        val ans = IntArray(queries.size)
        for (q in queries.indices) {
            val start = queries[q][0]
            val step = queries[q][1]
            if (step < block) {
                ans[q] = dp[step][start]
            } else {
                var total = 0L
                var i = start
                while (i < n) {
                    total += nums[i]
                    i += step
                }
                ans[q] = (total % mod).toInt()
            }
        }
        return ans
    }
}
