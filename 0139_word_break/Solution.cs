// LeetCode 0139 - Word Break
// https://leetcode.com/problems/word-break/

using System.Collections.Generic;

public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        var words = new HashSet<string>(wordDict);
        var dp = new bool[s.Length + 1];
        dp[0] = true;
        for (int end = 1; end <= s.Length; end++)
            for (int start = 0; start < end; start++)
                if (dp[start] && words.Contains(s.Substring(start, end - start))) { dp[end] = true; break; }
        return dp[s.Length];
    }
}
