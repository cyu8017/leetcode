// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int vis, m;

    public int evenSumSubgraphs(int[] nums, int[][] edges) {
        int n = nums.length;
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        g = gg;
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        m = (1 << n) - 1;
        int ans = 0;
        for (int sub = 1; sub <= m; sub++) {
            int s = 0;
            for (int i = 0; i < n; i++) {
                if (((sub >> i) & 1) != 0) s += nums[i];
            }
            if (s % 2 != 0) continue;
            vis = m ^ sub;
            int start = 31 - Integer.numberOfLeadingZeros(sub);
            dfs(start);
            if (vis == m) ans++;
        }
        return ans;
    }

    private void dfs(int u) {
        vis |= 1 << u;
        for (int v : g[u]) {
            if (((vis >> v) & 1) == 0) dfs(v);
        }
    }
}
