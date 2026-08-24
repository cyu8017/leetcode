// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

class Solution {
    fun hasMatch(s: String, p: String): Boolean {
        var i = p.indexOf('*')
        var left = p.substring(0, i)
        var right = p.substring(i + 1)
        var li = s.indexOf(left)
        if (li < 0) return false
        return s.indexOf(right, li + left.length) >= 0
    }
}
