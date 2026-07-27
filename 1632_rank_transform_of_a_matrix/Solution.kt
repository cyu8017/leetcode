// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

class Solution {
    fun matrixRankTransform(matrix: Array<IntArray>): Array<IntArray> {
        val m = matrix.size
        val n = matrix[0].size
        val groups = HashMap<Int, MutableList<IntArray>>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                groups.getOrPut(matrix[i][j]) { mutableListOf() }.add(intArrayOf(i, j))
            }
        }
        val rank = IntArray(m + n)
        val ans = Array(m) { IntArray(n) }
        for (value in groups.keys.sorted()) {
            val parent = HashMap<Int, Int>()
            fun find(x: Int): Int {
                parent.putIfAbsent(x, x)
                if (parent[x] != x) parent[x] = find(parent[x]!!)
                return parent[x]!!
            }
            for (cell in groups[value]!!) {
                val a = find(cell[0])
                val b = find(m + cell[1])
                parent[a] = b
            }
            val best = HashMap<Int, Int>()
            for (cell in groups[value]!!) {
                val root = find(cell[0])
                best[root] = maxOf(best.getOrDefault(root, 0), rank[cell[0]], rank[m + cell[1]])
            }
            for (cell in groups[value]!!) {
                val r = best[find(cell[0])]!! + 1
                ans[cell[0]][cell[1]] = r
            }
            for (cell in groups[value]!!) {
                rank[cell[0]] = maxOf(rank[cell[0]], ans[cell[0]][cell[1]])
                rank[m + cell[1]] = maxOf(rank[m + cell[1]], ans[cell[0]][cell[1]])
            }
        }
        return ans
    }
}
