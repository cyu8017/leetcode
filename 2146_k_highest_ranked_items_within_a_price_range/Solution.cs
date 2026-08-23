// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

public class Solution {
    public IList<IList<int>> HighestRankedKItems(int[][] grid, int[] pricing, int[] start, int k) {
        int m = grid.Length, n = grid[0].Length;
        int low = pricing[0], high = pricing[1];
        bool[][] vis = new bool[m][];
        for (int i = 0; i < m; i++) vis[i] = new bool[n];
        var q = new Queue<(int r, int c, int d)>();
        q.Enqueue((start[0], start[1], 0));
        vis[start[0]][start[1]] = true;
        var cands = new List<(int d, int price, int r, int c)>();
        int[][] dirs = { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
        while (q.Count > 0) {
            var (r, c, d) = q.Dequeue();
            if (grid[r][c] >= low && grid[r][c] <= high)
                cands.Add((d, grid[r][c], r, c));
            foreach (var dir in dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0) {
                    vis[nr][nc] = true;
                    q.Enqueue((nr, nc, d + 1));
                }
            }
        }
        cands.Sort();
        if (k > cands.Count) k = cands.Count;
        var ans = new List<IList<int>>();
        for (int i = 0; i < k; i++) ans.Add(new List<int> { cands[i].r, cands[i].c });
        return ans;
    }
}
