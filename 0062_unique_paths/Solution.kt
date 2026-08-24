// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

class Solution {
    fun uniquePaths(m: Int, n: Int): Int {
        val row = IntArray(n) { 1 }

        for (r in 1 until m) {
            for (col in 1 until n) {
                row[col] += row[col - 1]
            }
        }

        return row[n - 1]
    }
}
