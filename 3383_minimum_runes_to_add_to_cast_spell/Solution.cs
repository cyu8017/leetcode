// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

using System.Collections.Generic;

public class Solution {
    public int MinRunesToAdd(int n, int[] crystals, int[] flowFrom, int[] flowTo) {
        var g = new List<int>[n];
        var rg = new List<int>[n];
        for (int i = 0; i < n; i++) { g[i] = new List<int>(); rg[i] = new List<int>(); }
        for (int i = 0; i < flowFrom.Length; i++) {
            int a = flowFrom[i], b = flowTo[i];
            g[a].Add(b);
            rg[b].Add(a);
        }
        bool[] vis = new bool[n];
        var order = new List<int>();
        void Dfs1(int u) {
            vis[u] = true;
            foreach (int v in g[u]) if (!vis[v]) Dfs1(v);
            order.Add(u);
        }
        for (int i = 0; i < n; i++) if (!vis[i]) Dfs1(i);
        int[] comp = new int[n];
        for (int i = 0; i < n; i++) comp[i] = -1;
        int cid = 0;
        void Dfs2(int u) {
            comp[u] = cid;
            foreach (int v in rg[u]) if (comp[v] == -1) Dfs2(v);
        }
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            if (comp[u] == -1) {
                Dfs2(u);
                cid++;
            }
        }
        bool[] hasCrystal = new bool[cid];
        foreach (int c in crystals) hasCrystal[comp[c]] = true;
        int[] indeg = new int[cid];
        for (int u = 0; u < n; u++) {
            foreach (int v in g[u]) {
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
