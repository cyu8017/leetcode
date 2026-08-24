// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

class Solution {
    fun knightDialer(n: Int): Int {
        val MOD = 1_000_000_007
        val moves = arrayOf(
            intArrayOf(4, 6), intArrayOf(6, 8), intArrayOf(7, 9), intArrayOf(4, 8), intArrayOf(0, 3, 9),
            intArrayOf(), intArrayOf(0, 1, 7), intArrayOf(2, 6), intArrayOf(1, 3), intArrayOf(2, 4)
        )
        var dp = LongArray(10) { 1 }
        repeat(n - 1) {
            val ndp = LongArray(10)
            for (i in 0 until 10)
                for (j in moves[i]) ndp[j] = (ndp[j] + dp[i]) % MOD
            dp = ndp
        }
        var ans = 0L
        for (x in dp) ans = (ans + x) % MOD
        return ans.toInt()
    }
}
