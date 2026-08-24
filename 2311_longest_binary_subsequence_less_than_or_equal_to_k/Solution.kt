// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution {
    fun longestSubsequence(s: String, k: Int): Int {
        var zeros = 0
        for (c in s) if (c == '0') zeros++
        var value = 0L
        var ones = 0
        var pow = 1L
        for (i in s.lastIndex downTo 0) {
            if (s[i] == '1') {
                if (!(pow > k || value + pow > k)) {
                    value += pow
                    ones++
                }
            }
            if (pow <= k) {
                if (pow > (1L shl 60)) pow = k + 1L
                else pow = pow shl 1
            }
        }
        return zeros + ones
    }
}
