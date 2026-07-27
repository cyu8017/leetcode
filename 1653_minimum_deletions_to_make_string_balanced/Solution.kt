// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution {
    fun minimumDeletions(s: String): Int {
        var b = 0
        var ans = 0
        for (c in s) {
            if (c == 'b') b++
            else ans = minOf(ans + 1, b)
        }
        return ans
    }
}
