// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution {
    fun longestContinuousSubstring(s: String): Int {
        var ans = 1
        var cur = 1
        for (i in 1 until s.length) {
            if (s[i] == s[i - 1] + 1) {
                cur++
                ans = maxOf(ans, cur)
            } else cur = 1
        }
        return ans
    }
}
