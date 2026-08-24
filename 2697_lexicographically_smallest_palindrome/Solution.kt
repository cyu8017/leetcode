// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
    fun makeSmallestPalindrome(s: String): String {
        val arr = s.toCharArray()
        val n = arr.size
        for (i in 0 until n / 2) {
            val c = minOf(arr[i], arr[n - 1 - i])
            arr[i] = c
            arr[n - 1 - i] = c
        }
        return String(arr)
    }
}
