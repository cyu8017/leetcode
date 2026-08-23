// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public boolean isPossible(int n, List<List<Integer>> edges) {
        int[] deg = new int[n + 1];
        Set<Integer>[] adj = new HashSet[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new HashSet<>();
        for (List<Integer> e : edges) {
            int u = e.get(0), v = e.get(1);
            deg[u]++;
            deg[v]++;
            adj[u].add(v);
            adj[v].add(u);
        }
        List<Integer> odd = new ArrayList<>();
        for (int i = 1; i <= n; i++) if (deg[i] % 2 == 1) odd.add(i);
        if (odd.isEmpty()) return true;
        if (odd.size() == 2) {
            int a = odd.get(0), b = odd.get(1);
            if (!adj[a].contains(b)) return true;
            for (int i = 1; i <= n; i++) {
                if (i != a && i != b && !adj[a].contains(i) && !adj[b].contains(i)) return true;
            }
            return false;
        }
        if (odd.size() == 4) {
            int a = odd.get(0), b = odd.get(1), c = odd.get(2), d = odd.get(3);
            return (!adj[a].contains(b) && !adj[c].contains(d)) ||
                   (!adj[a].contains(c) && !adj[b].contains(d)) ||
                   (!adj[a].contains(d) && !adj[b].contains(c));
        }
        return false;
    }
}
