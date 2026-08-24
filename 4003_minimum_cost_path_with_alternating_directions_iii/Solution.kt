// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

class Solution {
    fun minCost(m: Int, n: Int, penalty: Array<IntArray>): Long {
        val INF = 1L shl 60
        val dist = Array(m) { Array(n) { LongArray(2) { INF } } }
        dist[0][0][1] = 1
        val pq = java.util.PriorityQueue<LongArray>(compareBy { it[0] })
        pq.offer(longArrayOf(1, 0, 0, 1))
        val dirs = arrayOf(intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            val i = cur[1].toInt()
            val j = cur[2].toInt()
            val k = cur[3].toInt()
            if (i == m - 1 && j == n - 1) return d
            if (d > dist[i][j][k]) continue
            val p = penalty[i][j]
            var nd = d + p
            if (nd < dist[i][j][k xor 1]) {
                dist[i][j][k xor 1] = nd
                pq.offer(longArrayOf(nd, i.toLong(), j.toLong(), (k xor 1).toLong()))
            }
            for (idx in 0 until 4) {
                val x = i + dirs[idx][0]
                val y = j + dirs[idx][1]
                if (0 <= x && x < m && 0 <= y && y < n) {
                    nd = d + ((x + 1).toLong() * (y + 1) + (((idx and 1) xor k) * p))
                    if (nd < dist[x][y][k xor 1]) {
                        dist[x][y][k xor 1] = nd
                        pq.offer(longArrayOf(nd, x.toLong(), y.toLong(), (k xor 1).toLong()))
                    }
                }
            }
        }
        return -1
    }
}
