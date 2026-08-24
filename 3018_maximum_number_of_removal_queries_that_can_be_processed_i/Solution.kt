// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

class Solution {
    fun maximumProcessableQueries(nums: IntArray, queries: IntArray): Int {
        val n = nums.size
        val f = Array(n) { IntArray(n) }
        val m = queries.size
        for (i in 0 until n) {
            for (j in n - 1 downTo i) {
                if (i > 0) {
                    val t = if (f[i - 1][j] < m && nums[i - 1] >= queries[f[i - 1][j]]) 1 else 0
                    f[i][j] = maxOf(f[i][j], f[i - 1][j] + t)
                }
                if (j + 1 < n) {
                    val t = if (f[i][j + 1] < m && nums[j + 1] >= queries[f[i][j + 1]]) 1 else 0
                    f[i][j] = maxOf(f[i][j], f[i][j + 1] + t)
                }
                if (f[i][j] == m) return m
            }
        }
        var ans = 0
        for (i in 0 until n) {
            val t = if (f[i][i] < m && nums[i] >= queries[f[i][i]]) 1 else 0
            ans = maxOf(ans, f[i][i] + t)
        }
        return ans
    }
}
