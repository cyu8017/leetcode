// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private boolean[] sus;

    private void dfs(int u) {
        if (sus[u]) return;
        sus[u] = true;
        for (int v : g[u]) dfs(v);
    }

    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : invocations) g[e[0]].add(e[1]);
        sus = new boolean[n];
        dfs(k);
        for (int[] e : invocations) {
            if (!sus[e[0]] && sus[e[1]]) {
                List<Integer> ans = new ArrayList<>();
                for (int i = 0; i < n; i++) ans.add(i);
                return ans;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) if (!sus[i]) ans.add(i);
        return ans;
    }
}
