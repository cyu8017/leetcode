// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

using System.Collections.Generic;

public class Solution {
    public IList<string> GetLongestSubsequence(string[] words, int[] groups) {
        var ans = new List<string> { words[0] };
        int last = groups[0];
        for (int i = 1; i < words.Length; i++) {
            if (groups[i] != last) {
                ans.Add(words[i]);
                last = groups[i];
            }
        }
        return ans;
    }
}
