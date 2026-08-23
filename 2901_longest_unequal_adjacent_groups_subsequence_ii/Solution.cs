// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> GetWordsInLongestSubsequence(string[] words, int[] groups) {
        int n = words.Length;
        int[] dp = new int[n], prev = new int[n];
        for (int i = 0; i < n; i++) { dp[i] = 1; prev[i] = -1; }
        int Hamming(string a, string b) {
            if (a.Length != b.Length) return 100;
            int d = 0;
            for (int i = 0; i < a.Length; i++) if (a[i] != b[i]) d++;
            return d;
        }
        int best = 1, bestI = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] != groups[j] && Hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > best) {
                best = dp[i];
                bestI = i;
            }
        }
        var path = new List<string>();
        for (int i = bestI; i != -1; i = prev[i]) path.Add(words[i]);
        path.Reverse();
        return path;
    }
}
