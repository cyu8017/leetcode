// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

class Solution {
    fun countBinarySubstrings(s: String): Int {
        var prev = 0
        var cur = 1
        var ans = 0
        for (i in 1 until s.length) {
            if (s[i] == s[i - 1]) cur++
            else {
                ans += minOf(prev, cur)
                prev = cur
                cur = 1
            }
        }
        return ans + minOf(prev, cur)
    }
}
