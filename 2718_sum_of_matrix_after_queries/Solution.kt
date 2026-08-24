// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution {
    fun matrixSumQueries(n: Int, queries: Array<IntArray>): Long {
        val rowDone = BooleanArray(n)
        val colDone = BooleanArray(n)
        var rowsLeft = n
        var colsLeft = n
        var ans = 0L
        for (i in queries.size - 1 downTo 0) {
            val type = queries[i][0]
            val idx = queries[i][1]
            val `val` = queries[i][2]
            if (type == 0) {
                if (!rowDone[idx]) {
                    ans += 1L * `val` * colsLeft
                    rowDone[idx] = true
                    rowsLeft--
                }
            } else {
                if (!colDone[idx]) {
                    ans += 1L * `val` * rowsLeft
                    colDone[idx] = true
                    colsLeft--
                }
            }
        }
        return ans
    }
}
