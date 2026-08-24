// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution {
    fun findMissingAndRepeatedValues(grid: Array<IntArray>): IntArray {
        val n = grid.size
        val freq = IntArray(n * n + 1)
        for (i in 0 until n) {
            for (j in 0 until n) {
                freq[grid[i][j]]++
            }
        }
        var rep = 0
        var miss = 0
        for (i in 1..n * n) {
            if (freq[i] == 2) rep = i
            if (freq[i] == 0) miss = i
        }
        return intArrayOf(rep, miss)
    }
}
