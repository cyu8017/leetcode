// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

using System.Collections.Generic;

public class Solution {
    public int MaximumSafenessFactor(IList<IList<int>> grid) {
        int n = grid.Count;
        int[][] dist = new int[n][];
        for (int i = 0; i < n; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) dist[i][j] = -1;
        }
        var q = new Queue<(int, int)>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) { dist[i][j] = 0; q.Enqueue((i, j)); }
        int[][] dirs = { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
        while (q.Count > 0) {
            var (x, y) = q.Dequeue();
            foreach (var d in dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[x][y] + 1;
                    q.Enqueue((ni, nj));
                }
            }
        }
        bool Ok(int sf) {
            if (dist[0][0] < sf) return false;
            bool[][] seen = new bool[n][];
            for (int i = 0; i < n; i++) seen[i] = new bool[n];
            var st = new List<(int, int)> { (0, 0) };
            seen[0][0] = true;
            while (st.Count > 0) {
                var (x, y) = st[^1];
                st.RemoveAt(st.Count - 1);
                if (x == n - 1 && y == n - 1) return true;
                foreach (var d in dirs) {
                    int ni = x + d[0], nj = y + d[1];
                    if (ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf) {
                        seen[ni][nj] = true;
                        st.Add((ni, nj));
                    }
                }
            }
            return false;
        }
        int lo = 0, hi = n * n, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
}
