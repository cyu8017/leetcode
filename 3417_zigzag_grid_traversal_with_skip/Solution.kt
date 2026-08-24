// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

class Solution {
    fun zigzagTraversal(grid: Array<IntArray>): IntArray {
        var ans = ArrayList<Int>()
        var skip = false
        for (i in 0 until grid.size) {
            var row = grid[i]
            if (i % 2 == 0) {
                for (v in row) {
                    if (!skip) ans.add(v)
                    skip = !skip
                }
            } else {
                for (j in row.size - 1 downTo 0) {
                    if (!skip) ans.add(row[j])
                    skip = !skip
                }
            }
        }
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }
}
