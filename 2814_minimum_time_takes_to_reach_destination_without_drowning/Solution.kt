// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

import java.util.ArrayDeque

class Solution {
    fun minimumSeconds(land: MutableList<MutableList<String>>): Int {
        val m = land.size
        val n = land[0].size
        val INF = 1 shl 30
        val water = Array(m) { IntArray(n) { INF } }
        val wq = ArrayDeque<IntArray>()
        var sx = 0
        var sy = 0
        var dx = 0
        var dy = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                when (land[i][j]) {
                    "*" -> {
                        water[i][j] = 0
                        wq.offer(intArrayOf(i, j))
                    }
                    "S" -> {
                        sx = i
                        sy = j
                    }
                    "D" -> {
                        dx = i
                        dy = j
                    }
                }
            }
        }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (wq.isNotEmpty()) {
            val cur = wq.poll()
            val x = cur[0]
            val y = cur[1]
            for (d in dirs) {
                val ni = x + d[0]
                val nj = y + d[1]
                if (ni !in 0 until m || nj !in 0 until n) continue
                val cell = land[ni][nj]
                if (cell == "X" || cell == "D") continue
                if (water[ni][nj] > water[x][y] + 1) {
                    water[ni][nj] = water[x][y] + 1
                    wq.offer(intArrayOf(ni, nj))
                }
            }
        }
        val dist = Array(m) { IntArray(n) { -1 } }
        val q = ArrayDeque<IntArray>()
        q.offer(intArrayOf(sx, sy))
        dist[sx][sy] = 0
        while (q.isNotEmpty()) {
            val cur = q.poll()
            val x = cur[0]
            val y = cur[1]
            if (x == dx && y == dy) return dist[x][y]
            for (d in dirs) {
                val ni = x + d[0]
                val nj = y + d[1]
                if (ni !in 0 until m || nj !in 0 until n || dist[ni][nj] != -1) continue
                if (land[ni][nj] == "X") continue
                val nd = dist[x][y] + 1
                if (land[ni][nj] != "D" && nd >= water[ni][nj]) continue
                dist[ni][nj] = nd
                q.offer(intArrayOf(ni, nj))
            }
        }
        return -1
    }
}
