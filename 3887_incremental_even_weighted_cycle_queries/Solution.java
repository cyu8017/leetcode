// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

class Solution {
    private int[] parent, size, parity;

    private int[] find(int x) {
        if (parent[x] == x) return new int[] { x, 0 };
        int[] res = find(parent[x]);
        int root = res[0], p = res[1];
        parity[x] ^= p;
        parent[x] = root;
        return new int[] { root, parity[x] };
    }

    public int countValidEdges(int n, int[][] edges) {
        parent = new int[n];
        size = new int[n];
        parity = new int[n];
        for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
        int ans = 0;
        for (int[] e : edges) {
            int[] fu = find(e[0]);
            int[] fv = find(e[1]);
            int ru = fu[0], pu = fu[1], rv = fv[0], pv = fv[1];
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
