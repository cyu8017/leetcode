// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    fun countLetters(s: String): Int {
        var ans = 1
        var length = 1
        for (i in 1 until s.length) {
            length = if (s[i] == s[i - 1]) length + 1 else 1
            ans += length
        }
        return ans
    }
}
