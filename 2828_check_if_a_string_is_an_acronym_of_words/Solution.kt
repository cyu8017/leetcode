// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution {
    fun isAcronym(words: MutableList<String>, s: String): Boolean {
        if (words.size != s.length) return false
        for (i in 0 until words.size) {
            var w = words[i]
            if (w.isEmpty() || w[0] != s[i]) return false
        }
        return true
    }
}
