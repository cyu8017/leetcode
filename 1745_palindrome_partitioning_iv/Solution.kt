// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution {
    fun checkPartitioning(s: String): Boolean {
        val n = s.length
        val pal = Array(n) { BooleanArray(n) }
        for (i in n - 1 downTo 0) {
            for (j in i until n) {
                pal[i][j] = s[i] == s[j] && (j - i < 2 || pal[i + 1][j - 1])
            }
        }
        for (i in 0 until n - 2) {
            for (j in i + 1 until n - 1) {
                if (pal[0][i] && pal[i + 1][j] && pal[j + 1][n - 1]) {
                    return true
                }
            }
        }
        return false
    }
}
