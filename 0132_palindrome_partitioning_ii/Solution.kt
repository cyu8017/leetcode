// LeetCode 0132 - Palindrome Partitioning II
// https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution {
    fun minCut(s: String): Int {
        val n = s.length
        if (n == 0) return 0
        val isPalindrome = Array(n) { BooleanArray(n) }
        for (left in n - 1 downTo 0)
            for (right in left until n)
                isPalindrome[left][right] = s[left] == s[right] && (right - left < 2 || isPalindrome[left + 1][right - 1])
        val cuts = IntArray(n)
        for (end in 0 until n) {
            cuts[end] = end
            if (isPalindrome[0][end]) cuts[end] = 0
            else for (start in 0 until end) if (isPalindrome[start + 1][end]) cuts[end] = minOf(cuts[end], cuts[start] + 1)
        }
        return cuts[n - 1]
    }
}
