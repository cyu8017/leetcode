// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

class Solution {
    fun shortestSuperstring(words: Array<String>): String {
        val n = words.size
        val overlap = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i == j) continue
                val a = words[i]
                val b = words[j]
                for (k in minOf(a.length, b.length) downTo 1) {
                    if (a.substring(a.length - k) == b.substring(0, k)) {
                        overlap[i][j] = k
                        break
                    }
                }
            }
        }
        val N = 1 shl n
        val dp = Array(N) { arrayOfNulls<String>(n) }
        for (i in 0 until n) dp[1 shl i][i] = words[i]
        for (mask in 0 until N) {
            for (last in 0 until n) {
                if ((mask and (1 shl last)) == 0 || dp[mask][last] == null) continue
                for (nxt in 0 until n) {
                    if ((mask and (1 shl nxt)) != 0) continue
                    val cand = dp[mask][last]!! + words[nxt].substring(overlap[last][nxt])
                    val nmask = mask or (1 shl nxt)
                    if (dp[nmask][nxt] == null || cand.length < dp[nmask][nxt]!!.length)
                        dp[nmask][nxt] = cand
                }
            }
        }
        val full = N - 1
        var best: String? = null
        for (i in 0 until n) {
            if (dp[full][i] != null && (best == null || dp[full][i]!!.length < best.length))
                best = dp[full][i]
        }
        return best!!
    }
}
