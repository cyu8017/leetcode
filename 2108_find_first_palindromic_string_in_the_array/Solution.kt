// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution {
    fun firstPalindrome(words: Array<String>): String {
        for (w in words) {
            var ok: Boolean = true
            var l = 0, r = w.length - 1
            while (l < r)
                if (w[l] != w[r]) { ok = false; break; }
            if (ok) return w
            l++, r--
        }
        return ""
    }
}
