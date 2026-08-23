// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int ans;
    private int a;
    private List<Integer>[] g;

    public int minimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        int d1 = treeDiameter(edges1);
        int d2 = treeDiameter(edges2);
        return Math.max(Math.max(d1, d2), (d1 + 1) / 2 + (d2 + 1) / 2 + 1);
    }

    private int treeDiameter(int[][] edges) {
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            gg[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            gg[e[0]].add(e[1]);
            gg[e[1]].add(e[0]);
        }
        g = gg;
        ans = 0;
        a = 0;
        dfs(0, -1, 0);
        dfs(a, -1, 0);
        return ans;
    }

    private void dfs(int i, int fa, int t) {
        for (int j : g[i]) {
            if (j != fa) {
                dfs(j, i, t + 1);
            }
        }
        if (ans < t) {
            ans = t;
            a = i;
        }
    }
}
