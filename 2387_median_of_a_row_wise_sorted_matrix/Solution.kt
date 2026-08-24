// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

class Solution {
    fun matrixMedian(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var lo = 1
        var hi = 1_000_000
        val need = (m * n) / 2 + 1
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (countLE(grid, mid, n) >= need) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun countLE(grid: Array<IntArray>, x: Int, n: Int): Int {
        var cnt = 0
        for (row in grid) {
            var l = 0
            var r = n
            while (l < r) {
                val mid = (l + r) / 2
                if (row[mid] <= x) l = mid + 1 else r = mid
            }
            cnt += l
        }
        return cnt
    }
}
