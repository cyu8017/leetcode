// LeetCode 0139 - Word Break
// https://leetcode.com/problems/word-break/

class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val words = wordDict.toHashSet()
        val dp = BooleanArray(s.length + 1)
        dp[0] = true
        for (end in 1..s.length)
            for (start in 0 until end)
                if (dp[start] && s.substring(start, end) in words) { dp[end] = true; break }
        return dp[s.length]
    }
}
