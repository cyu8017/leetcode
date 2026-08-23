// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int signalSpeed;
    private List<int[]>[] g;

    private int dfs(int a, int fa, int ws) {
        int cnt = (ws % signalSpeed == 0) ? 1 : 0;
        for (int[] e : g[a]) {
            int b = e[0], w = e[1];
            if (b != fa) cnt += dfs(b, a, ws + w);
        }
        return cnt;
    }

    public int[] countPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        this.signalSpeed = signalSpeed;
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        this.g = g;
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[]{e[1], e[2]});
            g[e[1]].add(new int[]{e[0], e[2]});
        }
        int[] ans = new int[n];
        for (int a = 0; a < n; a++) {
            int s = 0;
            for (int[] e : g[a]) {
                int t = dfs(e[0], a, e[1]);
                ans[a] += s * t;
                s += t;
            }
        }
        return ans;
    }
}
