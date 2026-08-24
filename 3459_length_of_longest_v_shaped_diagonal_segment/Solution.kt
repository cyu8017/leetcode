// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

class Solution {
    private var m: Int = 0
    private var n: Int = 0
    private var grid: Array<IntArray>? = null
    private val dirs: Array<IntArray> = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}}
    private val nextDir: IntArray = {1, 2, 3, 0}
    private val memo = HashMap<Long, Int>()

    fun lenOfVDiagonal(grid: Array<IntArray>): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        memo.clear()
        var ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] != 1) continue
                for (d in 0 until 4) {
                    var ni = i + dirs[d][0]
                    var nj = j + dirs[d][1]
                    var best = 1 + dfs(ni, nj, d, 0, 2)
                    if (best > ans) ans = best
                }
                if (ans < 1) ans = 1
            }
        }
        return ans
    }

    private fun key(i: Int, j: Int, d: Int, turned: Int, expect: Int): Long {
        return ((((i * 101L + j) * 5L + d) * 3L + turned) * 5L + expect)
    }

    private fun dfs(i: Int, j: Int, d: Int, turned: Int, expect: Int): Int {
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect) return 0
        var k = key(i, j, d, turned, expect)
        var cached = memo[k]
        if (cached != null) return cached
        var ni = i + dirs[d][0]
        var nj = j + dirs[d][1]
        var nx = if ((expect == 2)) 0 else 2
        var best = 1 + dfs(ni, nj, d, turned, nx)
        if (turned == 0) {
            var nd = nextDir[d]
            var ti = i + dirs[nd][0]
            var tj = j + dirs[nd][1]
            var cand = 1 + dfs(ti, tj, nd, 1, nx)
            if (cand > best) best = cand
        }
        memo[k] = best
        return best
    }
}
