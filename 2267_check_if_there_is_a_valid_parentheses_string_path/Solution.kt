// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

class Solution {
    private var m = 0
    private var n = 0
    private lateinit var grid: Array<CharArray>
    private lateinit var vis: HashSet<Long>

    private fun dfs(r: Int, c: Int, bal0: Int): Boolean {
        if (r >= m || c >= n) return false
        var bal = bal0 + if (grid[r][c] == '(') 1 else -1
        if (bal < 0) return false
        if (r == m - 1 && c == n - 1) return bal == 0
        val k = ((r.toLong() * n + c) shl 10) or bal.toLong()
        if (!vis.add(k)) return false
        return dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
    }

    fun hasValidPath(grid: Array<CharArray>): Boolean {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        if ((m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false
        vis = HashSet()
        return dfs(0, 0, 0)
    }
}
