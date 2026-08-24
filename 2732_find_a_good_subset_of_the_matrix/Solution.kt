// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

class Solution {
    fun goodSubsetofBinaryMatrix(grid: Array<IntArray>): MutableList<Int> {
        val n = grid[0].size
        val first = HashMap<Int, Int>()
        for (i in grid.indices) {
            var mask = 0
            for (j in 0 until n) if (grid[i][j] == 1) mask = mask or (1 shl j)
            if (mask == 0) return mutableListOf(i)
            for ((key, value) in first) {
                if ((key and mask) == 0) {
                    val a = value
                    val b = i
                    return if (a < b) mutableListOf(a, b) else mutableListOf(b, a)
                }
            }
            first.putIfAbsent(mask, i)
        }
        return ArrayList()
    }
}
