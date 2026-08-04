// LeetCode 1926
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution {
    fun nearestExit(maze: Array<CharArray>, entrance: IntArray): Int {
        val m = maze.size
        val n = maze[0].size
        val er = entrance[0]
        val ec = entrance[1]
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(er, ec, 0))
        maze[er][ec] = '+'
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val r = cur[0]
            val c = cur[1]
            val d = cur[2]
            for (dir in dirs) {
                val nr = r + dir[0]
                val nc = c + dir[1]
                if (nr in 0 until m && nc in 0 until n && maze[nr][nc] == '.') {
                    if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) return d + 1
                    maze[nr][nc] = '+'
                    q.add(intArrayOf(nr, nc, d + 1))
                }
            }
        }
        return -1
    }
}
