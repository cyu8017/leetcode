// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

class Solution {
    fun countSubIslands(grid1: Array<IntArray>, grid2: Array<IntArray>): Int {
        val rows = grid2.size
        val cols = grid2[0].size
        fun dfs(r: Int, c: Int): Boolean {
            if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0) return true
            grid2[r][c] = 0
            var ok = grid1[r][c] == 1
            for ((nr, nc) in listOf(r + 1 to c, r - 1 to c, r to c + 1, r to c - 1)) {
                if (!dfs(nr, nc)) ok = false
            }
            return ok
        }
        var ans = 0
        for (r in 0 until rows) for (c in 0 until cols) {
            if (grid2[r][c] == 1 && dfs(r, c)) ans++
        }
        return ans
    }
}
