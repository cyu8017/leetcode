// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
    fun longestSemiRepetitiveSubstring(s: String): Int {
        var ans = 0
        var left = 0
        var lastPair = -1
        for (right in 0 until s.length) {
            if (right > 0 && s[right] == s[right - 1]) {
                if (lastPair >= left) left = lastPair + 1
                lastPair = right - 1
            }
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
