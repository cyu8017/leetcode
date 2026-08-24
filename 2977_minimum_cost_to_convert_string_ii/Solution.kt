// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

class Solution {
    fun minimumCost(source: String, target: String, original: Array<String>, changed: Array<String>, cost: IntArray): Long {
        val INF = 1L shl 60
        val ids = HashMap<String, Int>()
        for (i in original.indices) {
            ids.putIfAbsent(original[i], ids.size)
            ids.putIfAbsent(changed[i], ids.size)
        }
        val m = ids.size
        val dist = Array(m) { LongArray(m) { INF } }
        for (i in 0 until m) dist[i][i] = 0
        for (i in original.indices) {
            val u = ids[original[i]]!!
            val v = ids[changed[i]]!!
            val ww = cost[i].toLong()
            if (ww < dist[u][v]) dist[u][v] = ww
        }
        for (k in 0 until m) {
            for (i in 0 until m) {
                for (j in 0 until m) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
        }
        val n = source.length
        val dp = LongArray(n + 1) { INF }
        dp[0] = 0
        val lens = HashSet<Int>()
        for (key in ids.keys) lens.add(key.length)
        for (i in 0 until n) {
            if (dp[i] >= INF / 2) continue
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i]
            for (L in lens) {
                if (i + L > n) continue
                val ss = source.substring(i, i + L)
                val tt = target.substring(i, i + L)
                val iu = ids[ss] ?: continue
                val iv = ids[tt] ?: continue
                if (dist[iu][iv] < INF / 2) {
                    val cand = dp[i] + dist[iu][iv]
                    if (cand < dp[i + L]) dp[i + L] = cand
                }
            }
        }
        if (dp[n] >= INF / 2) return -1
        return dp[n]
    }
}
