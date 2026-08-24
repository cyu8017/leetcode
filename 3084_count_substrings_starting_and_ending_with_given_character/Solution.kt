// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution {
    fun countSubstrings(s: String, c: Char): Long {
        var cnt = 0
        for (i in 0 until s.length) { if (s[i] == c) cnt++ }
        return cnt * (cnt + 1) / 2
    }
}
