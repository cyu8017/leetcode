// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        var m = strs[0].length
        var dp = IntArray(m)
        dp.fill(1)
        for (j in 0 until m) {
            for (i in 0 until j) {
                var ok = true
                for (row in strs) {
                    if (row[i] > row[j]) { ok = false; break; }
                }
                if (ok) dp[j] = maxOf(dp[j], dp[i] + 1)
            }
        }
        var mx = 0
        for (x in dp) { mx = maxOf(mx, x); }
        return m - mx
    }
}
