// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

class Solution {
    fun minSkips(dist: IntArray, speed: Int, hoursBefore: Int): Int {
        val limit = hoursBefore.toLong() * speed
        val n = dist.size
        var dp = LongArray(n + 1) { Long.MAX_VALUE / 4 }
        dp[0] = 0L
        for (road in dist) {
            val nxt = LongArray(n + 1) { Long.MAX_VALUE / 4 }
            for (skips in 0 until n) {
                if (dp[skips] >= Long.MAX_VALUE / 4) continue
                nxt[skips] = minOf(
                    nxt[skips],
                    ((dp[skips] + road + speed - 1) / speed) * speed
                )
                nxt[skips + 1] = minOf(nxt[skips + 1], dp[skips] + road)
            }
            dp = nxt
        }
        for (skips in dp.indices) {
            if (dp[skips] <= limit) return skips
        }
        return -1
    }
}
