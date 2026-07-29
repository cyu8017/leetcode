// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

class Solution {
    fun colorBorder(grid: Array<IntArray>, row: Int, col: Int, color: Int): Array<IntArray> {
        val m = grid.size; val n = grid[0].size
        val original = grid[row][col]
        fun key(r: Int, c: Int) = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)
        val component = mutableSetOf<Long>()
        val stack = ArrayDeque<IntArray>()
        stack.addLast(intArrayOf(row, col))
        component.add(key(row, col))
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (stack.isNotEmpty()) {
            val cur = stack.removeLast()
            for (d in dirs) {
                val nr = cur[0] + d[0]; val nc = cur[1] + d[1]
                val k = key(nr, nc)
                if (nr in 0 until m && nc in 0 until n && grid[nr][nc] == original && component.add(k)) {
                    stack.addLast(intArrayOf(nr, nc))
                }
            }
        }
        val border = mutableListOf<Pair<Int, Int>>()
        for (k in component) {
            val r = (k shr 32).toInt(); val c = k.toInt()
            var isBorder = false
            for (d in dirs) {
                val nr = r + d[0]; val nc = c + d[1]
                if (nr !in 0 until m || nc !in 0 until n || key(nr, nc) !in component) {
                    isBorder = true
                    break
                }
            }
            if (isBorder) border.add(r to c)
        }
        for ((r, c) in border) grid[r][c] = color
        return grid
    }
}
