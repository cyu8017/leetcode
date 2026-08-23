// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

public class Solution {
    public int[][] ValidArrangement(int[][] pairs) {
        var g = new Dictionary<int, List<int>>();
        var indeg = new Dictionary<int, int>();
        var outdeg = new Dictionary<int, int>();
        foreach (var p in pairs) {
            int u = p[0], v = p[1];
            if (!g.ContainsKey(u)) g[u] = new List<int>();
            g[u].Add(v);
            outdeg[u] = outdeg.GetValueOrDefault(u) + 1;
            indeg[v] = indeg.GetValueOrDefault(v) + 1;
        }
        int start = pairs[0][0];
        foreach (var kv in outdeg) {
            if (kv.Value - indeg.GetValueOrDefault(kv.Key) == 1) { start = kv.Key; break; }
        }
        var path = new List<int>();
        void Dfs(int u) {
            if (!g.ContainsKey(u)) g[u] = new List<int>();
            while (g[u].Count > 0) {
                int v = g[u][g[u].Count - 1];
                g[u].RemoveAt(g[u].Count - 1);
                Dfs(v);
            }
            path.Add(u);
        }
        Dfs(start);
        path.Reverse();
        var ans = new List<int[]>();
        for (int i = 0; i + 1 < path.Count; i++) ans.Add(new[] { path[i], path[i + 1] });
        return ans.ToArray();
    }
}
