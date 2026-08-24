// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

class Solution {
    private var grid: Array<IntArray>? = null
    private var n: Int = 0

    fun largestIsland(grid: Array<IntArray>): Int {
        var grid = grid
        this.grid = grid
        n = grid.size
        var sizes = HashMap<Int, Int>()
        sizes[0] = 0
        var islandId = 2
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    sizes[islandId] = dfs(i, j, islandId)
                    islandId++
                }
            }
        }
        var ans = 0
        for (v in sizes.values()) { ans = maxOf(ans, v) }
        var dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1}
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] != 0) continue
                var seen = HashSet<Int>()
                var total = 1
                for (k in 0 until 4) {
                    var ni = i + dr[k]
                    var nj = j + dc[k]
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        var iid = grid[ni][nj]
                        if (iid > 1 && seen.add(iid)) total += sizes[iid]
                    }
                }
                ans = maxOf(ans, total)
            }
        }
        return ans
    }

    private fun dfs(r: Int, c: Int, iid: Int): Int {
        if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return 0
        grid[r][c] = iid
        return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid)
    }
}
