// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

using System.Collections.Generic;

public class Solution {
    public int[] CountPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        int n = edges.Length + 1;
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        int Dfs(int a, int fa, int ws) {
            int cnt = (ws % signalSpeed == 0) ? 1 : 0;
            foreach (var (b, w) in g[a])
                if (b != fa) cnt += Dfs(b, a, ws + w);
            return cnt;
        }
        int[] ans = new int[n];
        for (int a = 0; a < n; a++) {
            int s = 0;
            foreach (var (b, w) in g[a]) {
                int t = Dfs(b, a, w);
                ans[a] += s * t;
                s += t;
            }
        }
        return ans;
    }
}
