// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

public class Solution {
    public int[] FindBall(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] ans = new int[n];
        for (int start = 0; start < n; start++) {
            int col = start;
            for (int row = 0; row < m; row++) {
                int next = col + grid[row][col];
                if (next < 0 || next == n || grid[row][next] != grid[row][col]) {
                    col = -1;
                    break;
                }
                col = next;
            }
            ans[start] = col;
        }
        return ans;
    }
}
