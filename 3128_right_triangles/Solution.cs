// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

public class Solution {
    public long NumberOfRightTriangles(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[] rows = new int[m], cols = new int[n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                rows[i] += grid[i][j];
                cols[j] += grid[i][j];
            }
        long ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1)
                    ans += 1L * (rows[i] - 1) * (cols[j] - 1);
        return ans;
    }
}
