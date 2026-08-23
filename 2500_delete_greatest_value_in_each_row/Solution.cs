// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

using System;

public class Solution {
    public int DeleteGreatestValue(int[][] grid) {
        foreach (var row in grid) Array.Sort(row);
        int ans = 0, n = grid[0].Length;
        for (int c = 0; c < n; c++) {
            int mx = 0;
            foreach (var row in grid) if (row[c] > mx) mx = row[c];
            ans += mx;
        }
        return ans;
    }
}
