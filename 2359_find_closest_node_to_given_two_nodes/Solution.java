// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

import java.util.Arrays;

class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.length;
        int[] Dist(int start) {
            int[] d = new int[n];
            Arrays.fill(d, -1);
            int cur = start, step = 0;
            while (cur != -1 && d[cur] == -1) {
                d[cur] = step;
                cur = edges[cur];
                step++;
            }
            return d;
        }
        int[] d1 = Dist(node1), d2 = Dist(node2);
        int ans = -1, best = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (d1[i] == -1 || d2[i] == -1) continue;
            int mx = Math.max(d1[i], d2[i]);
            if (mx < best) { best = mx; ans = i; }
        }
        return ans;
    }
}
