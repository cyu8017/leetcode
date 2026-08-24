// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        val n = strs.size
        val m = strs[0].length
        var deleted = 0
        val sortedPair = BooleanArray(n - 1)
        for (c in 0 until m) {
            var bad = false
            for (r in 0 until n - 1) {
                if (!sortedPair[r] && strs[r][c] > strs[r + 1][c]) {
                    bad = true
                    break
                }
            }
            if (bad) {
                deleted++
                continue
            }
            for (r in 0 until n - 1) {
                if (strs[r][c] < strs[r + 1][c]) sortedPair[r] = true
            }
        }
        return deleted
    }
}
