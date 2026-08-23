// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

using System.Collections.Generic;

public class Solution {
    public int EqualPairs(int[][] grid) {
        int n = grid.Length;
        var freq = new Dictionary<string, int>();
        for (int i = 0; i < n; i++) {
            string key = string.Join(",", grid[i]);
            if (!freq.ContainsKey(key)) freq[key] = 0;
            freq[key]++;
        }
        int ans = 0;
        int[] col = new int[n];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) col[i] = grid[i][j];
            string key = string.Join(",", col);
            if (freq.TryGetValue(key, out int c)) ans += c;
        }
        return ans;
    }
}
