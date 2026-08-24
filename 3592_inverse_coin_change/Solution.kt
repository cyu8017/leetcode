// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

class Solution {
    fun findCoins(numWays: IntArray): IntArray {
        var n = numWays.size
        var dp = IntArray(n + 1)
        var coins = ArrayList<Int>()
        dp[0] = 1
        for (amt in 1..n) {
            var ways = numWays[amt - 1]
            if (dp[amt] == ways) continue
            if (dp[amt] + 1 == ways) {
                coins.add(amt)
                for (x in amt..n) { dp[x] += dp[x - amt] }
                if (dp[amt] != ways) return IntArray(0)
                continue
            }
            return IntArray(0)
        }
        return coins.stream().mapToInt(Integer::intValue).toArray()
    }
}
