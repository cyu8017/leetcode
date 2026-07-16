// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

class Solution {
    fun repeatedSubstringPattern(s: String): Boolean {
        val doubled = s + s
        return doubled.substring(1, s.length * 2 - 1).contains(s)
    }
}
