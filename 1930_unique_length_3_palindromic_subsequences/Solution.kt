// LeetCode 1930
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }
        for (i in s.indices) {
            val c = s[i] - 'a'
            if (first[c] == -1) first[c] = i
            last[c] = i
        }
        var ans = 0
        for (c in 0 until 26) {
            if (first[c] != -1 && last[c] - first[c] > 1) {
                ans += s.substring(first[c] + 1, last[c]).toSet().size
            }
        }
        return ans
    }
}
