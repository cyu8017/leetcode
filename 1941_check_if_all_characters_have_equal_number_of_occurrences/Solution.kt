// LeetCode 1941
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution {
    fun areOccurrencesEqual(s: String): Boolean {
        val freq = IntArray(26)
        for (c in s) freq[c - 'a']++
        val vals = freq.filter { it > 0 }
        return vals.all { it == vals[0] }
    }
}
