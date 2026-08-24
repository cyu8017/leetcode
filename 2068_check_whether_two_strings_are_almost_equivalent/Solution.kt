// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution {
    fun checkAlmostEquivalent(word1: String, word2: String): Boolean {
var freq: IntArray = IntArray(26)
for (i in 0 until word1.length) {
freq[word1[i] - 'a']++
freq[word2[i] - 'a']--
}
for (v in freq) {
if (v > 3 || v < -3) {
return false
}
}
return true
}
}
