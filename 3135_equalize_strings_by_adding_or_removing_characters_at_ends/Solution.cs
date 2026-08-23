// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

using System;

public class Solution {
    public int MinOperations(string initial, string target) {
        int m = initial.Length, n = target.Length;
        int[][] f = new int[m + 1][];
        for (int i = 0; i <= m; i++) f[i] = new int[n + 1];
        int mx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (initial[i] == target[j]) {
                    f[i + 1][j + 1] = f[i][j] + 1;
                    mx = Math.Max(mx, f[i + 1][j + 1]);
                }
            }
        }
        return m + n - 2 * mx;
    }
}
