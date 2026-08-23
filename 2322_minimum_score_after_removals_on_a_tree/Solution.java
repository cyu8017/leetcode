// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] nums, xorv, inT, outT;
    private int time;

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        this.nums = nums;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        xorv = new int[n];
        inT = new int[n];
        outT = new int[n];
        time = 0;
        dfs(0, -1);
        int total = xorv[0], ans = Integer.MAX_VALUE;
        for (int i = 1; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int a, b, c;
                if (isAncestor(i, j)) {
                    a = xorv[j];
                    b = xorv[i] ^ xorv[j];
                    c = total ^ xorv[i];
                } else if (isAncestor(j, i)) {
                    a = xorv[i];
                    b = xorv[j] ^ xorv[i];
                    c = total ^ xorv[j];
                } else {
                    a = xorv[i];
                    b = xorv[j];
                    c = total ^ xorv[i] ^ xorv[j];
                }
                int mx = Math.max(a, Math.max(b, c));
                int mn = Math.min(a, Math.min(b, c));
                ans = Math.min(ans, mx - mn);
            }
        }
        return ans;
    }

    private void dfs(int u, int p) {
        inT[u] = time++;
        xorv[u] = nums[u];
        for (int v : g[u]) if (v != p) {
            dfs(v, u);
            xorv[u] ^= xorv[v];
        }
        outT[u] = time;
    }

    private boolean isAncestor(int a, int b) {
        return inT[a] <= inT[b] && outT[b] <= outT[a];
    }
}
