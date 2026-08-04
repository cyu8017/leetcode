// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution {
    fun removePalindromeSub(s: String): Int {
        if (s.isEmpty()) return 0
        var i = 0
        var j = s.length - 1
        while (i < j) {
            if (s[i] != s[j]) return 2
            i++
            j--
        }
        return 1
    }
}
