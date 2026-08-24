// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

class Solution {
    private fun isPalindrome(s: String, left: Int, right: Int): Boolean {
        var left = left
        var right = right
        while (left < right) {
            if (s[left] != s[right]) return false
            left++
            right--
        }
        return true
    }

    fun validPalindrome(s: String): Boolean {
        var left = 0
        var right = s.length - 1
        while (left < right) {
            if (s[left] != s[right]) {
                return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)
            }
            left++
            right--
        }
        return true
    }
}
