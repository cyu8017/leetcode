// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution {
    fun longestDecomposition(text: String): Int {
        val n = text.length
        var ans = 0
        var i = 0
        while (i < n - i) {
            var found = false
            for (length in 1..(n - 2 * i) / 2) {
                if (text.substring(i, i + length) == text.substring(n - i - length, n - i)) {
                    ans += 2
                    i += length
                    found = true
                    break
                }
            }
            if (!found) {
                ans++
                break
            }
        }
        return ans
    }
}
