// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

class Solution {
    fun makePalindrome(s: String): Boolean {
        var diff = 0
        var i = 0
        var j = s.length - 1
        while (i < j) {
            if (s[i] != s[j]) {
                diff++
                if (diff > 2) return false
            }
            i++
            j--
        }
        return true
    }
}
