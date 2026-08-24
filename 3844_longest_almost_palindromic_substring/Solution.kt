// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

class Solution {
    fun almostPalindromic(s: String): Int {
        val n = s.length
        var ans = 0
        for (i in 0 until n) {
            ans = maxOf(ans, maxOf(expand(s, i, i), expand(s, i, i + 1)))
        }
        return ans
    }

    private fun expand(s: String, l0: Int, r0: Int): Int {
        val n = s.length
        var l = l0
        var r = r0
        while (l >= 0 && r < n && s[l] == s[r]) {
            l--
            r++
        }
        var l1 = l - 1
        var r1 = r
        var l2 = l
        var r2 = r + 1
        while (l1 >= 0 && r1 < n && s[l1] == s[r1]) {
            l1--
            r1++
        }
        while (l2 >= 0 && r2 < n && s[l2] == s[r2]) {
            l2--
            r2++
        }
        return minOf(n, maxOf(r1 - l1 - 1, r2 - l2 - 1))
    }
}
