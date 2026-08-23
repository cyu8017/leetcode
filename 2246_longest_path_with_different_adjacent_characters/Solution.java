// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int ans = 1;
    private List<Integer>[] g;
    private String s;

    private int dfs(int u) {
        int best1 = 0, best2 = 0;
        for (int v : g[u]) {
            int lenV = dfs(v);
            if (s.charAt(v) == s.charAt(u)) continue;
            if (lenV > best1) {
                best2 = best1;
                best1 = lenV;
            } else if (lenV > best2) best2 = lenV;
        }
        ans = Math.max(ans, 1 + best1 + best2);
        return 1 + best1;
    }

    public int longestPath(int[] parent, String s) {
        int n = parent.length;
        this.s = s;
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        g = gg;
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) g[parent[i]].add(i);
        ans = 1;
        dfs(0);
        return ans;
    }
}
