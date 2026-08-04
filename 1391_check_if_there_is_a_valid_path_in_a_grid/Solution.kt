// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution {
    fun hasValidPath(grid: Array<IntArray>): Boolean {
        val dirs = mapOf(
            1 to listOf(0 to -1, 0 to 1),
            2 to listOf(-1 to 0, 1 to 0),
            3 to listOf(0 to -1, 1 to 0),
            4 to listOf(0 to 1, 1 to 0),
            5 to listOf(0 to -1, -1 to 0),
            6 to listOf(0 to 1, -1 to 0),
        )
        val m = grid.size
        val n = grid[0].size
        val seen = mutableSetOf(0 to 0)
        val st = ArrayDeque<Pair<Int, Int>>()
        st.add(0 to 0)
        while (st.isNotEmpty()) {
            val (r, c) = st.removeLast()
            if (r == m - 1 && c == n - 1) return true
            for ((dr, dc) in dirs[grid[r][c]]!!) {
                val x = r + dr
                val y = c + dc
                if (x in 0 until m && y in 0 until n && (x to y) !in seen &&
                    (-dr to -dc) in dirs[grid[x][y]]!!
                ) {
                    seen.add(x to y)
                    st.add(x to y)
                }
            }
        }
        return false
    }
}
