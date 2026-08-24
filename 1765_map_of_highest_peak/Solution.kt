// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

import java.util.ArrayDeque

class Solution {
    fun highestPeak(isWater: Array<IntArray>): Array<IntArray> {
        val m = isWater.size
        val n = isWater[0].size
        val dist = Array(m) { IntArray(n) { -1 } }
        val queue = ArrayDeque<IntArray>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (isWater[i][j] == 1) {
                    dist[i][j] = 0
                    queue.add(intArrayOf(i, j))
                }
            }
        }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            val (i, j) = queue.poll()
            for (d in dirs) {
                val x = i + d[0]
                val y = j + d[1]
                if (x in 0 until m && y in 0 until n && dist[x][y] == -1) {
                    dist[x][y] = dist[i][j] + 1
                    queue.add(intArrayOf(x, y))
                }
            }
        }
        return dist
    }
}
