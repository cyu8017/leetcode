// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

class Solution {
    fun numberOfWays(numPeople: Int): Int {
        val mod = 1_000_000_007
        val dp = IntArray(numPeople + 1)
        dp[0] = 1
        var people = 2
        while (people <= numPeople) {
            var ways = 0L
            var left = 0
            while (left < people) {
                ways = (ways + dp[left].toLong() * dp[people - 2 - left]) % mod
                left += 2
            }
            dp[people] = ways.toInt()
            people += 2
        }
        return dp[numPeople]
    }
}
