// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

using System.Collections.Generic;

public class Solution {
    private class Trie {
        public Trie[] Child = new Trie[2];
    }

    private List<int>[] g;
    private long[] sum;
    private int[] values;
    private Trie root;
    private long ans;

    public long MaxXor(int n, int[][] edges, int[] values) {
        this.values = values;
        g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        sum = new long[n];
        DfsSum(0, -1);
        root = new Trie();
        ans = 0;
        Dfs(0, -1);
        return ans;
    }

    private long DfsSum(int u, int p) {
        long s = values[u];
        foreach (int v in g[u]) if (v != p) s += DfsSum(v, u);
        return sum[u] = s;
    }

    private void Insert(long x) {
        Trie cur = root;
        for (int b = 46; b >= 0; b--) {
            int bit = (int)((x >> b) & 1);
            if (cur.Child[bit] == null) cur.Child[bit] = new Trie();
            cur = cur.Child[bit];
        }
    }

    private long Query(long x) {
        Trie cur = root;
        if (cur.Child[0] == null && cur.Child[1] == null) return 0;
        long res = 0;
        for (int b = 46; b >= 0; b--) {
            int bit = (int)((x >> b) & 1);
            int want = bit ^ 1;
            if (cur.Child[want] != null) {
                res |= 1L << b;
                cur = cur.Child[want];
            } else if (cur.Child[bit] != null) {
                cur = cur.Child[bit];
            } else {
                return res;
            }
        }
        return res;
    }

    private void Dfs(int u, int p) {
        foreach (int v in g[u]) {
            if (v == p) continue;
            long xorv = Query(sum[v]);
            if (xorv > ans) ans = xorv;
            Dfs(v, u);
            Insert(sum[v]);
        }
    }
}
