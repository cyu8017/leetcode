// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

class Solution {
    fun constructGridLayout(n: Int, edges: Array<IntArray>): Array<IntArray> {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val deg = IntArray(n) { g[it].size }
        var start = 0
        for (i in 0 until n) {
            if (deg[i] == 1) {
                start = i
                break
            }
            if (deg[i] == 2) start = i
        }
        val vis = BooleanArray(n)
        val row = ArrayList<Int>()
        var cur = start
        var prev = -1
        while (true) {
            row.add(cur)
            vis[cur] = true
            var next = -1
            for (v in g[cur]) {
                if (v != prev && !vis[v] && deg[v] <= 3) {
                    next = v
                    if (deg[v] < 4) break
                }
            }
            if (next == -1) break
            prev = cur
            cur = next
        }
        var width = row.size
        var height = if (width != 0) n / width else n
        if (width == 0 || width * height != n) {
            for (w in 1..n) {
                if (n % w == 0) {
                    width = w
                    height = n / w
                    break
                }
            }
        }
        val grid = Array(height) { IntArray(width) }
        for (i in 0 until n) grid[i / width][i % width] = i
        return grid
    }
}
