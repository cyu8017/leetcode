// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

class Solution {
    fun canPermutePalindrome(s: String): Boolean {
        val counts = IntArray(26)
        for (char in s) {
            counts[char.code - 'a'.code]++
        }
        var odd = 0
        for (count in counts) {
            if (count % 2 != 0) {
                odd++
            }
        }
        return odd <= 1
    }
}
