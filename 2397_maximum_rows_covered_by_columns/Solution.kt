// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution {
    private lateinit var matrix: Array<IntArray>
    private var m = 0
    private var n = 0
    private var numSelect = 0
    private var ans = 0

    fun maximumRows(matrix: Array<IntArray>, numSelect: Int): Int {
        this.matrix = matrix
        this.numSelect = numSelect
        m = matrix.size
        n = matrix[0].size
        ans = 0
        dfs(0, 0, 0)
        return ans
    }

    private fun dfs(col: Int, chosen: Int, mask: Int) {
        if (chosen == numSelect) {
            var covered = 0
            for (i in 0 until m) {
                var ok = true
                for (j in 0 until n) {
                    if (matrix[i][j] == 1 && ((mask shr j) and 1) == 0) {
                        ok = false
                        break
                    }
                }
                if (ok) covered++
            }
            ans = maxOf(ans, covered)
            return
        }
        if (col == n) return
        dfs(col + 1, chosen + 1, mask or (1 shl col))
        dfs(col + 1, chosen, mask)
    }
}
