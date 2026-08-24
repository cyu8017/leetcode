// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
    fun firstCompleteIndex(arr: IntArray, mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val posR = IntArray(m * n + 1)
        val posC = IntArray(m * n + 1)
        for (i in 0 until m)
            for (j in 0 until n) {
                posR[mat[i][j]] = i
                posC[mat[i][j]] = j
            }
        val rowCnt = IntArray(m)
        val colCnt = IntArray(n)
        for (i in arr.indices) {
            val r = posR[arr[i]]
            val c = posC[arr[i]]
            rowCnt[r]++
            colCnt[c]++
            if (rowCnt[r] == n || colCnt[c] == m) return i
        }
        return -1
    }
}
