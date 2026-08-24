// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

class Solution {
    private fun bitsOnes(x: Int): Int {
        var c = 0
        while (x > 0) { c += x and 1; x = x shr 1; }
        return c
    }

    fun findMinimumTime(strength: MutableList<Int>, k: Int): Int {
        var n = strength.size
        val inf = 1_000_000_000
        var N = 1  shl  n
        var dp = IntArray(N)
        dp.fill(inf)
        dp[0] = 0
        for (mask in 0 until N) {
            if (dp[mask] == inf) continue
            var opened = bitsOnes(mask)
            var x = 1 + opened * k
            for (i in 0 until n) {
                if ((mask and (1  shl  i)) != 0) continue
                var t = (strength[i] + x - 1) / x
                var nmask = mask or (1  shl  i)
                if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t
            }
        }
        return dp[N - 1]
    }
}
