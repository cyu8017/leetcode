// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

using System;

public class Solution {
    public int ClosestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.Length;
        int[] Dist(int start) {
            int[] d = new int[n];
            Array.Fill(d, -1);
            int cur = start, step = 0;
            while (cur != -1 && d[cur] == -1) {
                d[cur] = step;
                cur = edges[cur];
                step++;
            }
            return d;
        }
        int[] d1 = Dist(node1), d2 = Dist(node2);
        int ans = -1, best = int.MaxValue;
        for (int i = 0; i < n; i++) {
            if (d1[i] == -1 || d2[i] == -1) continue;
            int mx = Math.Max(d1[i], d2[i]);
            if (mx < best) { best = mx; ans = i; }
        }
        return ans;
    }
}
