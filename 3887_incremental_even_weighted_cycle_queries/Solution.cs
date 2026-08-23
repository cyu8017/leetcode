// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

public class Solution {
    public int CountValidEdges(int n, int[][] edges) {
        var parent = new int[n];
        var size = new int[n];
        var parity = new int[n];
        for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }

        (int, int) Find(int x) {
            if (parent[x] == x) return (x, 0);
            var (root, p) = Find(parent[x]);
            parity[x] ^= p;
            parent[x] = root;
            return (root, parity[x]);
        }

        int ans = 0;
        foreach (var e in edges) {
            var (ru, pu) = Find(e[0]);
            var (rv, pv) = Find(e[1]);
            if (ru == rv) {
                if ((pu ^ pv) == e[2]) ans++;
                continue;
            }
            if (size[ru] < size[rv]) {
                int t = ru; ru = rv; rv = t;
                t = pu; pu = pv; pv = t;
            }
            parent[rv] = ru;
            parity[rv] = pu ^ pv ^ e[2];
            size[ru] += size[rv];
            ans++;
        }
        return ans;
    }
}
