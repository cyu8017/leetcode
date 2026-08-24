// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution {
    fun equalPairs(grid: Array<IntArray>): Int {
        val n = grid.size
        val freq = HashMap<String, Int>()
        for (i in 0 until n) {
            val key = grid[i].joinToString(",")
            freq[key] = freq.getOrDefault(key, 0) + 1
        }
        var ans = 0
        val col = IntArray(n)
        for (j in 0 until n) {
            for (i in 0 until n) col[i] = grid[i][j]
            ans += freq.getOrDefault(col.joinToString(","), 0)
        }
        return ans
    }
}
