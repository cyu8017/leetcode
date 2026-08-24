// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

class Solution {
    fun snail(nums: IntArray, rowsCount: Int, colsCount: Int): Array<IntArray> {
        if (rowsCount * colsCount != nums.size) return emptyArray()
        val ans = Array(rowsCount) { IntArray(colsCount) }
        var idx = 0
        for (c in 0 until colsCount) {
            if (c % 2 == 0) {
                for (r in 0 until rowsCount) ans[r][c] = nums[idx++]
            } else {
                for (r in rowsCount - 1 downTo 0) ans[r][c] = nums[idx++]
            }
        }
        return ans
    }
}
