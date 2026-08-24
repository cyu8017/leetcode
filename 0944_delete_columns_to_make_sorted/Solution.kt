// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        var ans = 0
        val m = strs[0].length
        val n = strs.size
        for (c in 0 until m) {
            for (r in 0 until n - 1) {
                if (strs[r][c] > strs[r + 1][c]) {
                    ans++
                    break
                }
            }
        }
        return ans
    }
}
