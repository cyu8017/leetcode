// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/


class Solution {
    fun findChampion(grid: Array<IntArray>): Int {
        val n = grid.size
        for (i in 0 until n) {
            var win = true
            for (j in 0 until n) {
                if (i != j && grid[i][j] == 0) {
                    win = false
                    break
                }
            }
            if (win) return i
        }
        return -1
    }
}
