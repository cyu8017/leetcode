// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution {
    fun minimumCost(source: String, target: String, original: Array<String>, changed: Array<String>, cost: IntArray): Long {
        val inf = 1L shl 60
        val dist = Array(26) { LongArray(26) { inf } }
        for (i in 0 until 26) dist[i][i] = 0
        for (i in original.indices) {
            val u = original[i][0] - 'a'
            val v = changed[i][0] - 'a'
            val ww = cost[i].toLong()
            if (ww < dist[u][v]) dist[u][v] = ww
        }
        for (k in 0 until 26) {
            for (i in 0 until 26) {
                for (j in 0 until 26) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
        }
        var ans = 0L
        for (i in source.indices) {
            val a = source[i] - 'a'
            val b = target[i] - 'a'
            if (dist[a][b] >= inf / 2) return -1
            ans += dist[a][b]
        }
        return ans
    }
}
