// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

using System.Collections.Generic;

public class Solution {
    public long SumRemoteness(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        bool[][] seen = new bool[m][];
        for (int i = 0; i < m; i++) seen[i] = new bool[n];
        int[][] dirs = { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
        long total = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] != -1) total += grid[i][j];
        long ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1 || seen[i][j]) continue;
                var q = new Queue<(int, int)>();
                q.Enqueue((i, j));
                seen[i][j] = true;
                long sum = 0;
                int cnt = 0;
                while (q.Count > 0) {
                    var (x, y) = q.Dequeue();
                    sum += grid[x][y];
                    cnt++;
                    foreach (var d in dirs) {
                        int ni = x + d[0], nj = y + d[1];
                        if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1) {
                            seen[ni][nj] = true;
                            q.Enqueue((ni, nj));
                        }
                    }
                }
                ans += (total - sum) * cnt;
            }
        }
        return ans;
    }
}
