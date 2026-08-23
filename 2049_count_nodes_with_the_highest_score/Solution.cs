// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

using System.Collections.Generic;

public class Solution {
    public int CountHighestScoreNodes(int[] parents) {
        int n = parents.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) children[parents[i]].Add(i);
        int[] size = new int[n];
        int Dfs(int u) {
            size[u] = 1;
            foreach (int v in children[u]) size[u] += Dfs(v);
            return size[u];
        }
        Dfs(0);
        long best = 0;
        int ans = 0;
        for (int u = 0; u < n; u++) {
            long score = 1;
            foreach (int v in children[u]) score *= size[v];
            int up = n - size[u];
            if (up > 0) score *= up;
            if (score > best) { best = score; ans = 1; }
            else if (score == best) ans++;
        }
        return ans;
    }
}
