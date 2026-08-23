// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

import java.util.*;

class Solution {
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]); }
        int[] dist1 = new int[n + 1], dist2 = new int[n + 1];
        Arrays.fill(dist1, -1);
        Arrays.fill(dist2, -1);
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] { 1, 0 });
        dist1[1] = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int u = cur[0], d = cur[1];
            for (int v : g[u]) {
                int nd = d + 1;
                if (dist1[v] == -1) { dist1[v] = nd; q.offer(new int[] { v, nd }); }
                else if (dist2[v] == -1 && nd > dist1[v]) { dist2[v] = nd; q.offer(new int[] { v, nd }); }
            }
        }
        int steps = dist2[n], ans = 0;
        for (int i = 0; i < steps; i++) {
            if ((ans / change) % 2 == 1) ans += change - ans % change;
            ans += time;
        }
        return ans;
    }
}
