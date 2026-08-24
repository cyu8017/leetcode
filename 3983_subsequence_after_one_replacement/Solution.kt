// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

class Solution {
    fun canMakeSubsequence(s: String, t: String): Boolean {
        var m = s.length
        var n = t.length
        var i0 = 0
        var i1 = 0
        var j = 0
        while (i1 < m && j < n) {
            if (s[i1] == t[j]) i1++
            if (i1 < i0 + 1) i1 = i0 + 1
            if (s[i0] == t[j]) i0++
            j++
        }
        return i1 == m
    }
}
