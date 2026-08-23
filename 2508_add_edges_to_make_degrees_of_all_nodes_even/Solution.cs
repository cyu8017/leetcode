// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

using System.Collections.Generic;

public class Solution {
    public bool IsPossible(int n, IList<IList<int>> edges) {
        int[] deg = new int[n + 1];
        var adj = new HashSet<int>[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new HashSet<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            deg[u]++;
            deg[v]++;
            adj[u].Add(v);
            adj[v].Add(u);
        }
        var odd = new List<int>();
        for (int i = 1; i <= n; i++) if (deg[i] % 2 == 1) odd.Add(i);
        if (odd.Count == 0) return true;
        if (odd.Count == 2) {
            int a = odd[0], b = odd[1];
            if (!adj[a].Contains(b)) return true;
            for (int i = 1; i <= n; i++) {
                if (i != a && i != b && !adj[a].Contains(i) && !adj[b].Contains(i)) return true;
            }
            return false;
        }
        if (odd.Count == 4) {
            int a = odd[0], b = odd[1], c = odd[2], d = odd[3];
            return (!adj[a].Contains(b) && !adj[c].Contains(d)) ||
                   (!adj[a].Contains(c) && !adj[b].Contains(d)) ||
                   (!adj[a].Contains(d) && !adj[b].Contains(c));
        }
        return false;
    }
}
