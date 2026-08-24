// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

class Solution {
    private var m = 0
    private var n = 0
    private var ans = 0
    private lateinit var grid: Array<IntArray>
    private lateinit var ones: MutableList<IntArray>

    private fun dfs(idx0: Int, flips: Int) {
        if (flips >= ans) return
        var idx = idx0
        while (idx < ones.size && grid[ones[idx][0]][ones[idx][1]] == 0) idx++
        if (idx == ones.size) {
            ans = flips
            return
        }
        val r = ones[idx][0]
        val c = ones[idx][1]
        val changed = mutableListOf<IntArray>()
        for (j in 0 until n) if (grid[r][j] == 1) {
            grid[r][j] = 0
            changed.add(intArrayOf(r, j))
        }
        dfs(idx + 1, flips + 1)
        for (p in changed) grid[p[0]][p[1]] = 1
        changed.clear()
        for (i in 0 until m) if (grid[i][c] == 1) {
            grid[i][c] = 0
            changed.add(intArrayOf(i, c))
        }
        dfs(idx + 1, flips + 1)
        for (p in changed) grid[p[0]][p[1]] = 1
    }

    fun removeOnes(grid: Array<IntArray>): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        ones = mutableListOf()
        for (i in 0 until m) for (j in 0 until n) if (grid[i][j] == 1) ones.add(intArrayOf(i, j))
        if (ones.isEmpty()) return 0
        ans = m + n
        dfs(0, 0)
        return ans
    }
}
