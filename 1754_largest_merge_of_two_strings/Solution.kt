// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution {
    fun largestMerge(word1: String, word2: String): String {
        var i = 0
        var j = 0
        val out = StringBuilder()
        while (i < word1.length && j < word2.length) {
            if (word1.substring(i) > word2.substring(j)) {
                out.append(word1[i])
                i++
            } else {
                out.append(word2[j])
                j++
            }
        }
        out.append(word1, i, word1.length)
        out.append(word2, j, word2.length)
        return out.toString()
    }
}
