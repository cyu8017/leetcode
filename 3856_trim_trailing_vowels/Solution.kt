// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

class Solution {
    fun trimTrailingVowels(s: String): String {
        var i = s.length - 1
        while (i >= 0 && isVowel(s[i])) i--
        return s.substring(0, i + 1)
    }

    private fun isVowel(c: Char): Boolean {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }
}
