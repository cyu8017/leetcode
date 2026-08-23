// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

public class Solution {
    public int MaximumDetonation(int[][] bombs) {
        int n = bombs.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 0; i < n; i++) {
            long x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                long dx = bombs[j][0] - x1, dy = bombs[j][1] - y1;
                if (dx * dx + dy * dy <= r1 * r1) g[i].Add(j);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            bool[] vis = new bool[n];
            var q = new Queue<int>();
            q.Enqueue(i); vis[i] = true;
            int cnt = 0;
            while (q.Count > 0) {
                int u = q.Dequeue();
                cnt++;
                foreach (int v in g[u]) if (!vis[v]) { vis[v] = true; q.Enqueue(v); }
            }
            ans = Math.Max(ans, cnt);
        }
        return ans;
    }
}
