// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

class Solution {
    private lateinit var g: Array<MutableList<Int>>
    private lateinit var match: IntArray

    private fun dfs(u: Int, seen: BooleanArray): Boolean {
        for (v in g[u]) {
            if (seen[v]) continue
            seen[v] = true
            if (match[v] == -1 || dfs(match[v], seen)) {
                match[v] = u
                return true
            }
        }
        return false
    }

    fun minimumOperations(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val id = Array(m) { IntArray(n) { -1 } }
        var cnt = 0
        for (i in 0 until m) for (j in 0 until n) if (grid[i][j] == 1) id[i][j] = cnt++
        g = Array(cnt) { mutableListOf() }
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] != 1 || (i + j) % 2 != 0) continue
                val u = id[i][j]
                for (d in dirs) {
                    val ni = i + d[0]
                    val nj = j + d[1]
                    if (ni in 0 until m && nj in 0 until n && grid[ni][nj] == 1) g[u].add(id[ni][nj])
                }
            }
        }
        match = IntArray(cnt) { -1 }
        var ans = 0
        for (u in 0 until cnt) {
            var ok = false
            loop@ for (i in 0 until m) for (j in 0 until n) {
                if (id[i][j] == u && (i + j) % 2 == 0) {
                    ok = true
                    break@loop
                }
            }
            if (!ok) continue
            if (dfs(u, BooleanArray(cnt))) ans++
        }
        return ans
    }
}
