// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

class Solution {
    fun createGrid(m: Int, n: Int, k: Int): Array<String> {
        val cands = ArrayList<Array<String>>()
        when (k) {
            1 -> cands.add(arrayOf("."))
            2 -> cands.add(arrayOf("..", ".."))
            3 -> {
                cands.add(arrayOf("..", "..", ".."))
                cands.add(arrayOf("...", "..."))
            }
            4 -> {
                cands.add(arrayOf("..", "..", "..", ".."))
                cands.add(arrayOf("....", "...."))
                cands.add(arrayOf("..#", "...", "#.."))
            }
        }
        for (pat in cands) {
            val pr = pat.size
            val pc = pat[0].length
            if (pr > m || pc > n) continue
            val result = Array(m) { "" }
            for (i in 0 until m) {
                val row = CharArray(n) { '#' }
                result[i] = String(row)
            }
            for (i in 0 until pr) {
                val row = result[i].toCharArray()
                for (j in 0 until pc) row[j] = pat[i][j]
                result[i] = String(row)
            }
            for (i in pr until m) {
                val row = result[i].toCharArray()
                row[pc - 1] = '.'
                result[i] = String(row)
            }
            for (j in pc until n) {
                val row = result[m - 1].toCharArray()
                row[j] = '.'
                result[m - 1] = String(row)
            }
            return result
        }
        return emptyArray()
    }
}
