// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

class Solution {
    private lateinit var grid: Array<IntArray>
    private var m = 0
    private var n = 0
    private var target = 0
    private lateinit var memo: HashMap<Long, Boolean>

    private fun key(r: Int, c: Int, bal: Int): Long =
        (r.toLong() shl 40) or (c.toLong() shl 20) or (bal.toLong() and 0xfffffL)

    private fun dfs(r: Int, c: Int, bal0: Int): Boolean {
        if (r >= m || c >= n) return false
        val bal = bal0 + grid[r][c]
        if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false
        if (r == m - 1 && c == n - 1) return bal == target
        val k = key(r, c, bal)
        memo[k]?.let { return it }
        val ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
        memo[k] = ok
        return ok
    }

    fun isThereAPath(grid: Array<IntArray>): Boolean {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        if ((m + n - 1) % 2 != 0) return false
        target = (m + n - 1) / 2
        memo = HashMap()
        return dfs(0, 0, 0)
    }
}
