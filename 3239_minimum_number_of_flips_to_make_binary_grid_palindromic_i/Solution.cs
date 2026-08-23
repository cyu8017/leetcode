// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

using System;

public class Solution {
    public int MinFlips(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int cnt1 = 0, cnt2 = 0;
        foreach (var row in grid) {
            for (int j = 0; j < n / 2; j++) {
                if (row[j] != row[n - j - 1]) cnt1++;
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m / 2; i++) {
                if (grid[i][j] != grid[m - i - 1][j]) cnt2++;
            }
        }
        return Math.Min(cnt1, cnt2);
    }
}
