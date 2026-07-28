// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

using System.Collections.Generic;

public class Solution {
    public int[][] IndexPairs(string text, string[] words) {
        var wordSet = new HashSet<string>(words);
        var ans = new List<int[]>();
        int n = text.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (wordSet.Contains(text.Substring(i, j - i + 1))) {
                    ans.Add(new[] { i, j });
                }
            }
        }
        return ans.ToArray();
    }
}
