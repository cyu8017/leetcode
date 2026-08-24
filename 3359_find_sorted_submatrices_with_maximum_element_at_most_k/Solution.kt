// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

class Solution {
    fun countSortedMatrices(grid: Array<IntArray>, k: Int): Long {
        val m = grid.size
        val n = grid[0].size
        var ans = 0L
        for (r1 in 0 until m) {
            for (r2 in r1 until m) {
                for (c1 in 0 until n) {
                    for (c2 in c1 until n) {
                        var ok = true
                        var i = r1
                        while (i <= r2 && ok) {
                            for (j in c1..c2) {
                                if (grid[i][j] > k) {
                                    ok = false
                                    break
                                }
                                if (j > c1 && grid[i][j] < grid[i][j - 1]) {
                                    ok = false
                                    break
                                }
                                if (i > r1 && grid[i][j] < grid[i - 1][j]) {
                                    ok = false
                                    break
                                }
                            }
                            i++
                        }
                        if (ok) ans++
                    }
                }
            }
        }
        return ans
    }
}
