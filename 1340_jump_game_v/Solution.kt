// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

class Solution {
    fun maxJumps(arr: IntArray, d: Int): Int {
        val n = arr.size
        val dp = IntArray(n) { 1 }
        val order = arr.indices.sortedBy { arr[it] }
        for (i in order) {
            for (step in intArrayOf(-1, 1)) {
                var j = i + step
                while (j in 0 until n && kotlin.math.abs(j - i) <= d && arr[j] < arr[i]) {
                    dp[i] = maxOf(dp[i], 1 + dp[j])
                    j += step
                }
            }
        }
        return dp.maxOrNull() ?: 1
    }
}
