// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

public class Solution {
    public int[][] LargestLocal(int[][] grid) {
        int n = grid.Length;
        var ans = new int[n - 2][];
        for (int i = 0; i < n - 2; i++) {
            ans[i] = new int[n - 2];
            for (int j = 0; j < n - 2; j++) {
                int mx = 0;
                for (int r = i; r < i + 3; r++)
                    for (int c = j; c < j + 3; c++)
                        if (grid[r][c] > mx) mx = grid[r][c];
                ans[i][j] = mx;
            }
        }
        return ans;
    }
}
