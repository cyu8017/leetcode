// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

import java.util.PriorityQueue

class Solution {
    fun swimInWater(grid: Array<IntArray>): Int {
        val n = grid.size
        val heap = PriorityQueue(compareBy<IntArray> { it[0] })
        val seen = Array(n) { BooleanArray(n) }
        heap.offer(intArrayOf(grid[0][0], 0, 0))
        seen[0][0] = true
        val dirs = arrayOf(
            intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1)
        )
        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val time = cur[0]
            val r = cur[1]
            val c = cur[2]
            if (r == n - 1 && c == n - 1) return time
            for (d in dirs) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr in 0 until n && nc in 0 until n && !seen[nr][nc]) {
                    seen[nr][nc] = true
                    val nt = maxOf(time, grid[nr][nc])
                    heap.offer(intArrayOf(nt, nr, nc))
                }
            }
        }
        return -1
    }
}
