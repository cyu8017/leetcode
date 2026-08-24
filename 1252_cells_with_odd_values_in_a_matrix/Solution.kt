// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
    fun oddCells(m: Int, n: Int, indices: Array<IntArray>): Int {
        val rows = IntArray(m)
        val cols = IntArray(n)
        for (idx in indices) {
            rows[idx[0]] = rows[idx[0]] xor 1
            cols[idx[1]] = cols[idx[1]] xor 1
        }
        var answer = 0
        for (r in 0 until m) {
            for (c in 0 until n) answer += rows[r] xor cols[c]
        }
        return answer
    }
}
