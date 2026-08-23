// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

import java.util.Arrays;

class Solution {
    public int deleteGreatestValue(int[][] grid) {
        for (var row : grid) Arrays.sort(row);
        int ans = 0, n = grid[0].length;
        for (int c = 0; c < n; c++) {
            int mx = 0;
            for (var row : grid) if (row[c] > mx) mx = row[c];
            ans += mx;
        }
        return ans;
    }
}
