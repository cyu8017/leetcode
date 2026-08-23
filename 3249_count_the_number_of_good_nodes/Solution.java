// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int ans;

    public int countGoodNodes(int[][] edges) {
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        for (int i = 0; i < n; i++) gg[i] = new ArrayList<>();
        g = gg;
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        ans = 0;
        dfs(0, -1);
        return ans;
    }

    private int dfs(int a, int fa) {
        int pre = -1, cnt = 1, ok = 1;
        for (int b : g[a]) {
            if (b != fa) {
                int cur = dfs(b, a);
                cnt += cur;
                if (pre < 0) pre = cur;
                else if (pre != cur) ok = 0;
            }
        }
        ans += ok;
        return cnt;
    }
}
