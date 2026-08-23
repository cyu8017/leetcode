// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

class Solution {
    public int uniquePaths(int m, int n) {
        int[] row = new int[n];
        for (int i = 0; i < n; i++) {
            row[i] = 1;
        }

        for (int r = 1; r < m; r++) {
            for (int col = 1; col < n; col++) {
                row[col] += row[col - 1];
            }
        }

        return row[n - 1];
    }
}
