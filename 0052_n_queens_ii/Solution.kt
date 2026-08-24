// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

class Solution {
    fun totalNQueens(n: Int): Int {
        var count = 0
        val cols = HashSet<Int>()
        val diag1 = HashSet<Int>()
        val diag2 = HashSet<Int>()

        fun backtrack(row: Int) {
            if (row == n) {
                count++
                return
            }

            for (col in 0 until n) {
                if (col in cols || row + col in diag1 || row - col in diag2) {
                    continue
                }

                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
            }
        }

        backtrack(0)
        return count
    }
}
