// LeetCode 0131 - Palindrome Partitioning
// https://leetcode.com/problems/palindrome-partitioning/

class Solution {
    fun partition(s: String): List<List<String>> {
        val result = mutableListOf<List<String>>()
        fun isPalindrome(leftStart: Int, rightStart: Int): Boolean {
            var left = leftStart
            var right = rightStart
            while (left < right) if (s[left++] != s[right--]) return false
            return true
        }
        fun dfs(start: Int, path: MutableList<String>) {
            if (start == s.length) { result.add(path.toList()); return }
            for (end in start until s.length) if (isPalindrome(start, end)) {
                path.add(s.substring(start, end + 1))
                dfs(end + 1, path)
                path.removeAt(path.lastIndex)
            }
        }
        dfs(0, mutableListOf())
        return result
    }
}
