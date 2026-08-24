// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

class Solution {
    fun rotate(grid: Array<IntArray>): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val t = Array(n) { IntArray(m) }
        for (i in 0 until m) for (j in 0 until n) t[j][i] = grid[i][j]
        return t
    }

    fun check(g: Array<IntArray>): Boolean {
        val m = g.size
        val n = g[0].size
        var s1 = 0L
        var s2 = 0L
        val cnt1 = HashMap<Long, Int>()
        val cnt2 = HashMap<Long, Int>()
        for (row in g) for (x in row) {
            val v = x.toLong()
            s2 += v
            cnt2[v] = cnt2.getOrDefault(v, 0) + 1
        }
        for (i in 0 until m - 1) {
            for (x in g[i]) {
                val v = x.toLong()
                s1 += v
                s2 -= v
                cnt1[v] = cnt1.getOrDefault(v, 0) + 1
                cnt2[v] = cnt2[v]!! - 1
            }
            if (s1 == s2) return true
            if (s1 < s2) {
                val diff = s2 - s1
                if (cnt2.getOrDefault(diff, 0) > 0) {
                    if ((m - i - 1 > 1 && n > 1) ||
                        (i == m - 2 && (g[i + 1][0].toLong() == diff || g[i + 1][n - 1].toLong() == diff)) ||
                        (n == 1 && (g[i + 1][0].toLong() == diff || g[m - 1][0].toLong() == diff))
                    ) return true
                }
            } else {
                val diff = s1 - s2
                if (cnt1.getOrDefault(diff, 0) > 0) {
                    if ((i + 1 > 1 && n > 1) ||
                        (i == 0 && (g[0][0].toLong() == diff || g[0][n - 1].toLong() == diff)) ||
                        (n == 1 && (g[0][0].toLong() == diff || g[i][0].toLong() == diff))
                    ) return true
                }
            }
        }
        return false
    }

    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        return check(grid) || check(rotate(grid))
    }
}
