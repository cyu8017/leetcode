// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

class Solution {
    fun longestCommonPrefix(s: String, t: String): Int {
        var i = 0
        var j = 0
        var removed = false
        while (i < s.length && j < t.length) {
            if (s[i] == t[j]) {
                i = i + 1
                j = j + 1
                continue
            }
            if (removed) break
            removed = true
            i = i + 1
        }
        return j
    }
}
