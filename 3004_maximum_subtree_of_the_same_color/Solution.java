// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] colors, size;
    private int ans;

    private boolean dfs(int a, int fa) {
        size[a] = 1;
        boolean ok = true;
        for (int b : g[a]) {
            if (b != fa) {
                boolean t = dfs(b, a);
                ok = ok && t && colors[a] == colors[b];
                size[a] += size[b];
            }
        }
        if (ok) ans = Math.max(ans, size[a]);
        return ok;
    }

    public int maximumSubtreeSize(int[][] edges, int[] colors) {
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        for (int i = 0; i < n; i++) gg[i] = new ArrayList<>();
        for (int[] e : edges) {
            gg[e[0]].add(e[1]);
            gg[e[1]].add(e[0]);
        }
        this.g = gg;
        this.colors = colors;
        this.size = new int[n];
        this.ans = 0;
        dfs(0, -1);
        return ans;
    }
}
