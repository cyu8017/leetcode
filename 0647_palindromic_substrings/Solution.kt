// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/


class Solution {
    fun countSubstrings(s: String): Int {
        var count = 0
        for (center in 0 until 2 * s.length - 1) {
            var left = center / 2
            var right = left + center % 2
            while (left >= 0 && right < s.length && s[left] == s[right]) {
                count++
                left--
                right++
            }
        }
        return count
    }
}
