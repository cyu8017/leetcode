// LeetCode 1986
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution {
    fun minSessions(tasks: IntArray, sessionTime: Int): Int {
        val n = tasks.size
        val inf = n + 1 to 0
        val dp = Array(1 shl n) { inf }
        dp[0] = 1 to 0
        for (mask in 0 until (1 shl n)) {
            val (sessions, used) = dp[mask]
            if (sessions > n) continue
            for (i in 0 until n) {
                if (mask and (1 shl i) != 0) continue
                val t = tasks[i]
                val nmask = mask or (1 shl i)
                val cand = if (used + t <= sessionTime) sessions to used + t else sessions + 1 to t
                if (cand.first < dp[nmask].first ||
                    (cand.first == dp[nmask].first && cand.second < dp[nmask].second)
                ) dp[nmask] = cand
            }
        }
        return dp[(1 shl n) - 1].first
    }
}
