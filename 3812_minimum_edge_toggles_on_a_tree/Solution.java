// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum_edge_toggles_on_a_tree/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private List<int[]>[] g;
    private String start, target;
    private List<Integer> ans;

    public int[] minimumFlips(int n, int[][] edges, String start, String target) {
        this.start = start;
        this.target = target;
        g = newList(n);
        for (int i = 0; i < n - 1; i++) {
            int a = edges[i][0], b = edges[i][1];
            g[a].add(new int[]{b, i});
            g[b].add(new int[]{a, i});
        }
        ans = new ArrayList<>();
        if (dfs(0, -1)) return new int[]{-1};
        Collections.sort(ans);
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }

    private boolean dfs(int a, int fa) {
        boolean rev = start.charAt(a) != target.charAt(a);
        for (int[] e : g[a]) {
            int b = e[0], i = e[1];
            if (b != fa && dfs(b, a)) {
                ans.add(i);
                rev = !rev;
            }
        }
        return rev;
    }

    @SuppressWarnings("unchecked")
    private List<int[]>[] newList(int n) {
        List<int[]>[] g = (List<int[]>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
