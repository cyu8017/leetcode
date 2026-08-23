// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestCycle(int[] edges) {
        int n = edges.length;
        boolean[] vis = new boolean[n];
        int ans = -1;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            Map<Integer, Integer> dist = new HashMap<>();
            int cur = i, step = 0;
            while (cur != -1 && !vis[cur]) {
                vis[cur] = true;
                dist.put(cur, step);
                cur = edges[cur];
                step++;
            }
            if (cur != -1 && dist.containsKey(cur)) {
                ans = Math.max(ans, step - dist.get(cur));
            }
        }
        return ans;
    }
}
