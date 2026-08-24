
// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
    fun rowAndMaximumOnes(mat: Array<IntArray>): IntArray {
        var bestRow = 0
        var bestCnt = -1
        for (i in mat.indices) {
            var cnt = 0
            for (v in mat[i]) cnt += v
            if (cnt > bestCnt) {
                bestCnt = cnt
                bestRow = i
            }
        }
        return intArrayOf(bestRow, bestCnt)
    }
}
