// LeetCode 1466 - Reorder Routes To Make All Paths Lead To The City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

import java.util.*;

class Solution {
    public int minReorder(int n, int[][] connections) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : connections) {
            graph.get(e[0]).add(new int[]{e[1], 1});
            graph.get(e[1]).add(new int[]{e[0], 0});
        }
        int ans = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        boolean[] seen = new boolean[n];
        stack.push(0);
        seen[0] = true;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            for (int[] edge : graph.get(node)) {
                int nei = edge[0], cost = edge[1];
                if (!seen[nei]) {
                    seen[nei] = true;
                    stack.push(nei);
                    ans += cost;
                }
            }
        }
        return ans;
    }
}
