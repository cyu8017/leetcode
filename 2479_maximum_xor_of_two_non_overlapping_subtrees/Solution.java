// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static class Trie {
        Trie[] child = new Trie[2];
    }

    private List<Integer>[] g;
    private int[] values;
    private long[] sum;
    private Trie root;
    private long ans;

    private long dfsSum(int u, int p) {
        long s = values[u];
        for (int v : g[u]) if (v != p) s += dfsSum(v, u);
        return sum[u] = s;
    }

    private void insert(long x) {
        Trie cur = root;
        for (int b = 46; b >= 0; b--) {
            int bit = (int) ((x >> b) & 1);
            if (cur.child[bit] == null) cur.child[bit] = new Trie();
            cur = cur.child[bit];
        }
    }

    private long query(long x) {
        Trie cur = root;
        if (cur.child[0] == null && cur.child[1] == null) return 0;
        long res = 0;
        for (int b = 46; b >= 0; b--) {
            int bit = (int) ((x >> b) & 1);
            int want = bit ^ 1;
            if (cur.child[want] != null) {
                res |= 1L << b;
                cur = cur.child[want];
            } else if (cur.child[bit] != null) {
                cur = cur.child[bit];
            } else {
                return res;
            }
        }
        return res;
    }

    private void dfs(int u, int p) {
        for (int v : g[u]) {
            if (v == p) continue;
            long xorv = query(sum[v]);
            if (xorv > ans) ans = xorv;
            dfs(v, u);
            insert(sum[v]);
        }
    }

    public long maxXor(int n, int[][] edges, int[] values) {
        this.values = values;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        sum = new long[n];
        dfsSum(0, -1);
        root = new Trie();
        ans = 0;
        dfs(0, -1);
        return ans;
    }
}
