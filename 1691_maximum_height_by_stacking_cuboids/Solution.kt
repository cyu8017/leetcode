// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution {
    fun maxHeight(cuboids: Array<IntArray>): Int {
        val a = cuboids.map { it.sorted().toIntArray() }.sortedWith(
            compareBy({ it[0] }, { it[1] }, { it[2] })
        )
        val n = a.size
        val dp = IntArray(n)
        for (i in 0 until n) {
            dp[i] = a[i][2]
            for (j in 0 until i) {
                if ((0 until 3).all { d -> a[j][d] <= a[i][d] }) {
                    dp[i] = maxOf(dp[i], dp[j] + a[i][2])
                }
            }
        }
        return dp.maxOrNull() ?: 0
    }
}
