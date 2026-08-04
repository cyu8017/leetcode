// LeetCode 1997
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

class Solution {
    fun firstDayBeenInAllRooms(nextVisit: IntArray): Int {
        val mod = 1_000_000_007L
        val n = nextVisit.size
        val dp = LongArray(n)
        for (i in 1 until n) {
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2 + mod * 2) % mod
        }
        return dp[n - 1].toInt()
    }
}
