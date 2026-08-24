// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution {
    fun findSubstringInWraproundString(s: String): Int {
        val counts = IntArray(26)
        var length = 0
        for (index in s.indices) {
            length = if (index > 0 && (s[index] - s[index - 1] + 26) % 26 == 1) {
                length + 1
            } else {
                1
            }
            val position = s[index] - 'a'
            counts[position] = maxOf(counts[position], length)
        }
        return counts.sum()
    }
}
