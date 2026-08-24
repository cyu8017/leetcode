// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

class Solution {
    private lateinit var parent: IntArray

    fun regionsBySlashes(grid: Array<String>): Int {
        val n = grid.size
        parent = IntArray(n * n * 4) { it }
        for (r in 0 until n) {
            for (c in 0 until n) {
                val root = 4 * (r * n + c)
                val ch = grid[r][c]
                when (ch) {
                    '/' -> {
                        unite(root + 0, root + 3)
                        unite(root + 1, root + 2)
                    }
                    '\\' -> {
                        unite(root + 0, root + 1)
                        unite(root + 2, root + 3)
                    }
                    else -> {
                        unite(root + 0, root + 1)
                        unite(root + 1, root + 2)
                        unite(root + 2, root + 3)
                    }
                }
                if (r + 1 < n) unite(root + 2, root + 4 * n + 0)
                if (c + 1 < n) unite(root + 1, root + 4 + 3)
            }
        }
        var ans = 0
        for (i in parent.indices) if (find(i) == i) ans++
        return ans
    }

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        parent[find(a)] = find(b)
    }
}
