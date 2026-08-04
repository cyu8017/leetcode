// LeetCode 1901 - Find A Peak Element Ii
// https://leetcode.com/problems/find-a-peak-element-ii/

class Solution {
    fun findPeakGrid(mat: Array<IntArray>): IntArray {
        val rows = mat.size
        val cols = mat[0].size
        var lo = 0
        var hi = cols - 1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            var maxRow = 0
            for (r in 1 until rows) if (mat[r][mid] > mat[maxRow][mid]) maxRow = r
            val left = if (mid > 0) mat[maxRow][mid - 1] else -1
            val right = if (mid + 1 < cols) mat[maxRow][mid + 1] else -1
            if (mat[maxRow][mid] >= left && mat[maxRow][mid] >= right) return intArrayOf(maxRow, mid)
            if (left > mat[maxRow][mid]) hi = mid - 1 else lo = mid + 1
        }
        return intArrayOf(0, 0)
    }
}
