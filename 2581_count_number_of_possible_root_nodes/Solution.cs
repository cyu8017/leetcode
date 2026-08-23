// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

using System.Collections.Generic;

public class Solution {
    public int RootCount(int[][] edges, int[][] guesses, int k) {
        int n = edges.Length + 1;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        var guessSet = new HashSet<(int, int)>();
        foreach (var gu in guesses) guessSet.Add((gu[0], gu[1]));
        int Dfs1(int u, int p) {
            int cnt = 0;
            foreach (int v in g[u]) {
                if (v == p) continue;
                if (guessSet.Contains((u, v))) cnt++;
                cnt += Dfs1(v, u);
            }
            return cnt;
        }
        int baseCnt = Dfs1(0, -1);
        int ans = 0;
        void Dfs2(int u, int p, int cur) {
            if (cur >= k) ans++;
            foreach (int v in g[u]) {
                if (v == p) continue;
                int nxt = cur;
                if (guessSet.Contains((u, v))) nxt--;
                if (guessSet.Contains((v, u))) nxt++;
                Dfs2(v, u, nxt);
            }
        }
        Dfs2(0, -1, baseCnt);
        return ans;
    }
}
