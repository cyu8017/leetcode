// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

import java.util.*;

class Solution {
    private List<Integer>[] children;
    private int[] size;

    public int countHighestScoreNodes(int[] parents) {
        int n = parents.length;
        children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) children[parents[i]].add(i);
        size = new int[n];
        dfs(0);
        long best = 0;
        int ans = 0;
        for (int u = 0; u < n; u++) {
            long score = 1;
            for (int v : children[u]) score *= size[v];
            int up = n - size[u];
            if (up > 0) score *= up;
            if (score > best) { best = score; ans = 1; }
            else if (score == best) ans++;
        }
        return ans;
    }

    private int dfs(int u) {
        size[u] = 1;
        for (int v : children[u]) size[u] += dfs(v);
        return size[u];
    }
}
