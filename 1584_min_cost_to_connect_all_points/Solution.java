// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] used = new boolean[n];
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = 1_000_000_000;
        }
        dist[0] = 0;
        int answer = 0;
        for (int t = 0; t < n; t++) {
            int u = -1;
            for (int i = 0; i < n; i++) {
                if (!used[i] && (u == -1 || dist[i] < dist[u])) {
                    u = i;
                }
            }
            used[u] = true;
            answer += dist[u];
            for (int v = 0; v < n; v++) {
                if (!used[v]) {
                    int d = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
                    if (d < dist[v]) {
                        dist[v] = d;
                    }
                }
            }
        }
        return answer;
    }
}
