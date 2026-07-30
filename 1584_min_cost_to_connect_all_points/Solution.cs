// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

using System;

public class Solution {
    public int MinCostConnectPoints(int[][] points) {
        int n = points.Length;
        bool[] used = new bool[n];
        int[] dist = new int[n];
        Array.Fill(dist, int.MaxValue);
        dist[0] = 0;
        int answer = 0;
        for (int step = 0; step < n; step++) {
            int u = -1;
            for (int i = 0; i < n; i++)
                if (!used[i] && (u == -1 || dist[i] < dist[u])) u = i;
            used[u] = true;
            answer += dist[u];
            for (int v = 0; v < n; v++) {
                if (used[v]) continue;
                int d = Math.Abs(points[u][0] - points[v][0]) + Math.Abs(points[u][1] - points[v][1]);
                dist[v] = Math.Min(dist[v], d);
            }
        }
        return answer;
    }
}
