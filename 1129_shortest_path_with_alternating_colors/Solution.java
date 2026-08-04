// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        List<Integer>[][] graph = new List[2][n];
        for (int c = 0; c < 2; c++) for (int i = 0; i < n; i++) graph[c][i] = new ArrayList<>();
        for (int[] e : redEdges) graph[0][e[0]].add(e[1]);
        for (int[] e : blueEdges) graph[1][e[0]].add(e[1]);
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] seen = new boolean[n][2];
        queue.offer(new int[]{0, 0, 0});
        queue.offer(new int[]{0, 1, 0});
        seen[0][0] = seen[0][1] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int node = cur[0], color = cur[1], dist = cur[2];
            if (ans[node] == -1) ans[node] = dist;
            int nextColor = 1 - color;
            for (int nxt : graph[color][node]) {
                if (!seen[nxt][nextColor]) {
                    seen[nxt][nextColor] = true;
                    queue.offer(new int[]{nxt, nextColor, dist + 1});
                }
            }
        }
        return ans;
    }
}
