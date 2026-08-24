// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        val out = StringBuilder()
        var i = 0
        var j = 0
        while (i < word1.length || j < word2.length) {
            if (i < word1.length) {
                out.append(word1[i])
                i++
            }
            if (j < word2.length) {
                out.append(word2[j])
                j++
            }
        }
        return out.toString()
    }
}
