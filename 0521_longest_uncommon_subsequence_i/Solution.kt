// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution {
    fun findLUSlength(a: String, b: String): Int {
        return if (a == b) -1 else maxOf(a.length, b.length)
    }
}
