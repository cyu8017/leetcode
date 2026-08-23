// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

import java.util.*;

class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        int target = (1 << n) - 1;
        Queue<int[]> queue = new ArrayDeque<>();
        Set<Long> seen = new HashSet<>();
        for (int i = 0; i < n; i++) {
            queue.offer(new int[] {i, 1 << i, 0});
            seen.add(((long) i << 20) | (1 << i));
        }
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int node = cur[0], mask = cur[1], dist = cur[2];
            if (mask == target) return dist;
            for (int nxt : graph[node]) {
                int nmask = mask | (1 << nxt);
                long state = ((long) nxt << 20) | nmask;
                if (seen.add(state)) queue.offer(new int[] {nxt, nmask, dist + 1});
            }
        }
        return -1;
    }
}
