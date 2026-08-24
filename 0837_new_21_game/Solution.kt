// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

class Solution {
    fun new21Game(n: Int, k: Int, maxPts: Int): Double {
        if (k == 0 || n >= k - 1 + maxPts) return 1.0
        var dp = DoubleArray(n + 1)
        dp[0] = 1.0
        var window = 1.0
        var ans = 0.0
        for (i in 1 until = n) {
            dp[i] = window / maxPts
            if (i < k) window += dp[i]
            else ans += dp[i]
            if (i - maxPts >= 0 && i - maxPts < k) window -= dp[i - maxPts]
        }
        return ans
    }
}
