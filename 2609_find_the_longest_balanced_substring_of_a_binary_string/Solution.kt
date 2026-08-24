// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution {
    fun findTheLongestBalancedSubstring(s: String): Int {
        var ans = 0
        var zeros = 0
        var ones = 0
        for (c in s.toCharArray()) {
            if (c == '0') {
                if (ones > 0) zeros = ones = 0
                zeros = zeros + 1
            } else {
                ones = ones + 1
                var cur = minOf(ones, zeros)
                if (2 * cur > ans) ans = 2 * cur
            }
        }
        return ans
    }
}
