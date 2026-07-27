// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution {
    fun closeStrings(word1: String, word2: String): Boolean {
        if (word1.length != word2.length) return false
        val a = IntArray(26)
        val b = IntArray(26)
        for (c in word1) a[c - 'a']++
        for (c in word2) b[c - 'a']++
        for (i in 0 until 26) {
            if ((a[i] == 0) != (b[i] == 0)) return false
        }
        a.sort()
        b.sort()
        return a.contentEquals(b)
    }
}
