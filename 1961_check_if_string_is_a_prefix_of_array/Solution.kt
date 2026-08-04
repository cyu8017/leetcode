// LeetCode 1961
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution {
    fun isPrefixString(s: String, words: Array<String>): Boolean {
        val built = StringBuilder()
        for (w in words) {
            built.append(w)
            val cur = built.toString()
            if (cur == s) return true
            if (cur.length > s.length || !s.startsWith(cur)) return false
        }
        return false
    }
}
