// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private List<Integer>[] g, rg;
    private boolean[] vis;
    private List<Integer> order;
    private int[] comp;
    private int cid;

    private void dfs1(int u) {
        vis[u] = true;
        for (int v : g[u]) if (!vis[v]) dfs1(v);
        order.add(u);
    }

    private void dfs2(int u) {
        comp[u] = cid;
        for (int v : rg[u]) if (comp[v] == -1) dfs2(v);
    }

    public int minRunesToAdd(int n, int[] crystals, int[] flowFrom, int[] flowTo) {
        g = new ArrayList[n];
        rg = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            g[i] = new ArrayList<>();
            rg[i] = new ArrayList<>();
        }
        for (int i = 0; i < flowFrom.length; i++) {
            int a = flowFrom[i], b = flowTo[i];
            g[a].add(b);
            rg[b].add(a);
        }
        vis = new boolean[n];
        order = new ArrayList<>();
        for (int i = 0; i < n; i++) if (!vis[i]) dfs1(i);
        comp = new int[n];
        Arrays.fill(comp, -1);
        cid = 0;
        for (int i = n - 1; i >= 0; i--) {
            int u = order.get(i);
            if (comp[u] == -1) {
                dfs2(u);
                cid++;
            }
        }
        boolean[] hasCrystal = new boolean[cid];
        for (int c : crystals) hasCrystal[comp[c]] = true;
        int[] indeg = new int[cid];
        for (int u = 0; u < n; u++) {
            for (int v : g[u]) {
                if (comp[u] != comp[v]) indeg[comp[v]]++;
            }
        }
        int ans = 0;
        for (int i = 0; i < cid; i++) {
            if (indeg[i] == 0 && !hasCrystal[i]) ans++;
        }
        return ans;
    }
}
