// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution {
    fun createGrid(m: Int, n: Int): Array<String> {
        val g = Array(m) { "" }
        for (i in 0 until m) {
            val row = CharArray(n) { '#' }
            if (i == 0) for (j in 0 until n) row[j] = '.'
            row[n - 1] = '.'
            g[i] = String(row)
        }
        return g
    }
}
