// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

class Solution {
    fun camelMatch(queries: Array<String>, pattern: String): List<Boolean> =
        queries.map { matches(it, pattern) }

    private fun matches(q: String, pattern: String): Boolean {
        var i = 0
        for (ch in q) {
            if (i < pattern.length && ch == pattern[i]) i++
            else if (ch in 'A'..'Z') return false
        }
        return i == pattern.length
    }
}
