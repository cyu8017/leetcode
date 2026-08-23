// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

import java.util.*;

class Solution {
    public int maximumInvitations(int[] favorite) {
        int n = favorite.length;
        int[] indeg = new int[n], depth = new int[n];
        Arrays.fill(depth, 1);
        for (int f : favorite) indeg[f]++;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.offer(i);
        while (!q.isEmpty()) {
            int u = q.poll();
            int v = favorite[u];
            depth[v] = Math.max(depth[v], depth[u] + 1);
            if (--indeg[v] == 0) q.offer(v);
        }
        int pairSum = 0, maxCycle = 0;
        boolean[] vis = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0 || vis[i]) continue;
            int u = i, lenCycle = 0;
            while (!vis[u]) {
                vis[u] = true;
                u = favorite[u];
                lenCycle++;
            }
            if (lenCycle == 2) pairSum += depth[i] + depth[favorite[i]];
            else maxCycle = Math.max(maxCycle, lenCycle);
        }
        return Math.max(pairSum, maxCycle);
    }
}
