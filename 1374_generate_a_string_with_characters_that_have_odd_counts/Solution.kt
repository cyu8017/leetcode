// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution {
    fun generateTheString(n: Int): String {
        return if (n % 2 == 1) "a".repeat(n) else "a".repeat(n - 1) + "b"
    }
}
