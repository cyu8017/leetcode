// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

class Solution {
    fun BitsOnes(x: Int): Int {
        var c = 0
        while (x > 0) {
            c += x and 1
            x = x shr 1
        }
        return c
    }

    fun findMinimumTime(strength: IntArray): Int {
        var n = strength.size
        var N = 1  shl  n
        val inf = 1e18
        var dp = LongArray(N)
        for (i in 0 until N) { dp[i] = inf }
        dp[0] = 0
        var k = 1
        for (mask in 0 until N) {
            if (dp[mask] == inf) continue
            var opened = BitsOnes(mask)
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
