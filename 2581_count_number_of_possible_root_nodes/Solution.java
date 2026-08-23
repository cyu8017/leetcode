// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    private List<Integer>[] g;
    private Set<Long> guessSet;
    private int ans, k;

    public int rootCount(int[][] edges, int[][] guesses, int k) {
        this.k = k;
        int n = edges.length + 1;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        guessSet = new HashSet<>();
        for (int[] gu : guesses) guessSet.add(pack(gu[0], gu[1]));
        int baseCnt = dfs1(0, -1);
        ans = 0;
        dfs2(0, -1, baseCnt);
        return ans;
    }

    private long pack(int a, int b) {
        return ((long) a << 32) | (b & 0xffffffffL);
    }

    private int dfs1(int u, int p) {
        int cnt = 0;
        for (int v : g[u]) {
            if (v == p) continue;
            if (guessSet.contains(pack(u, v))) cnt++;
            cnt += dfs1(v, u);
        }
        return cnt;
    }

    private void dfs2(int u, int p, int cur) {
        if (cur >= k) ans++;
        for (int v : g[u]) {
            if (v == p) continue;
            int nxt = cur;
            if (guessSet.contains(pack(u, v))) nxt--;
            if (guessSet.contains(pack(v, u))) nxt++;
            dfs2(v, u, nxt);
        }
    }
}
