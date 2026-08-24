// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/


class Solution {
    fun checkRecord(n: Int): Int {
        val MOD = 1_000_000_007
        var dp = arrayOf(longArrayOf(1, 0, 0), longArrayOf(0, 0, 0))
        repeat(n) {
            val nxt = Array(2) { LongArray(3) }
            for (a in 0 until 2) {
                for (l in 0 until 3) {
                    val ways = dp[a][l]
                    if (ways == 0L) continue
                    nxt[a][0] = (nxt[a][0] + ways) % MOD
                    if (a == 0) nxt[1][0] = (nxt[1][0] + ways) % MOD
                    if (l < 2) nxt[a][l + 1] = (nxt[a][l + 1] + ways) % MOD
                }
            }
            dp = nxt
        }
        var total = 0L
        for (a in 0 until 2) for (l in 0 until 3) total = (total + dp[a][l]) % MOD
        return total.toInt()
    }
}
