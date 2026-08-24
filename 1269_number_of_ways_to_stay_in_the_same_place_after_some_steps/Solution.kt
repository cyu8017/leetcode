// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution {
    fun numWays(steps: Int, arrLen: Int): Int {
        val mod = 1_000_000_007
        val width = minOf(arrLen, steps / 2 + 1)
        var dp = IntArray(width)
        dp[0] = 1
        repeat(steps) {
            val next = IntArray(width)
            for (i in 0 until width) {
                next[i] = dp[i]
                if (i > 0) next[i] = (next[i] + dp[i - 1]) % mod
                if (i + 1 < width) next[i] = (next[i] + dp[i + 1]) % mod
            }
            dp = next
        }
        return dp[0]
    }
}
