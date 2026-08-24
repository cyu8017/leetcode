// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

class Solution {
    fun maximumStrength(nums: IntArray, k: Int): Long {
        val n = nums.size
        val INF = Long.MIN_VALUE / 2
        val f = Array(n + 1) { Array(k + 1) { LongArray(2) { INF } } }
        f[0][0][0] = 0
        for (i in 1..n) {
            val x = nums[i - 1].toLong()
            for (j in 0..k) {
                val sign = if ((j and 1) != 0) 1L else -1L
                val `val` = sign * x * (k - j + 1)
                f[i][j][0] = maxOf(f[i - 1][j][0], f[i - 1][j][1])
                f[i][j][1] = maxOf(f[i][j][1], f[i - 1][j][1] + `val`)
                if (j > 0) {
                    val t = maxOf(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + `val`
                    f[i][j][1] = maxOf(f[i][j][1], t)
                }
            }
        }
        return maxOf(f[n][k][0], f[n][k][1])
    }
}
