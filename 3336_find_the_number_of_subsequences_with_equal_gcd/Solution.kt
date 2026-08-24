// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

class Solution {
    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        if (a == 0) return b
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    fun subsequencePairCount(nums: IntArray): Int {
        val mod = 1_000_000_007
        var maxV = 0
        for (x in nums) if (x > maxV) maxV = x
        var dp = Array(maxV + 1) { IntArray(maxV + 1) }
        dp[0][0] = 1
        for (x in nums) {
            val ndp = Array(maxV + 1) { IntArray(maxV + 1) }
            for (a in 0..maxV) {
                System.arraycopy(dp[a], 0, ndp[a], 0, maxV + 1)
            }
            for (a in 0..maxV) {
                for (b in 0..maxV) {
                    if (dp[a][b] == 0) continue
                    val na = if (a == 0) x else gcd(a, x)
                    val nb = if (b == 0) x else gcd(b, x)
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
                }
            }
            dp = ndp
        }
        var ans = 0
        for (g in 1..maxV) ans = (ans + dp[g][g]) % mod
        return ans
    }
}
