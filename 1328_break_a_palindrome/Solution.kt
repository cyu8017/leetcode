// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

class Solution {
    fun breakPalindrome(palindrome: String): String {
        if (palindrome.length == 1) return ""
        val chars = palindrome.toCharArray()
        for (i in 0 until chars.size / 2) {
            if (chars[i] != 'a') {
                chars[i] = 'a'
                return String(chars)
            }
        }
        chars[chars.lastIndex] = 'b'
        return String(chars)
    }
}
