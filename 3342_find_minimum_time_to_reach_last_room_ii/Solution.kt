// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

import java.util.PriorityQueue

class Solution {
    fun minTimeToReach(moveTime: Array<IntArray>): Int {
        val m = moveTime.size
        val n = moveTime[0].size
        val INF = 1 shl 30
        val dist = Array(m) { Array(n) { IntArray(2) { INF } } }
        val pq = PriorityQueue<IntArray>(compareBy { it[0] })
        dist[0][0][0] = 0
        pq.offer(intArrayOf(0, 0, 0, 0))
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val t = cur[0]
            val r = cur[1]
            val c = cur[2]
            val parity = cur[3]
            if (t != dist[r][c][parity]) continue
            if (r == m - 1 && c == n - 1) return t
            val cost = if (parity == 1) 2 else 1
            for (d in dirs) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue
                val start = maxOf(t, moveTime[nr][nc])
                val nt = start + cost
                val np = 1 - parity
                if (nt < dist[nr][nc][np]) {
                    dist[nr][nc][np] = nt
                    pq.offer(intArrayOf(nt, nr, nc, np))
                }
            }
        }
        return -1
    }
}
