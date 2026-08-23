// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    private int[][] points;
    private int n;

    private int dist(int i, int j) {
        return Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
    }

    private boolean ok(int d) {
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (dist(i, j) < d) {
                    g[i].add(j);
                    g[j].add(i);
                }
            }
        }
        int[] color = new int[n];
        for (int i = 0; i < n; i++) color[i] = -1;
        for (int i = 0; i < n; i++) {
            if (color[i] != -1) continue;
            Queue<Integer> q = new ArrayDeque<>();
            q.offer(i);
            color[i] = 0;
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : g[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        q.offer(v);
                    } else if (color[v] == color[u]) return false;
                }
            }
        }
        return true;
    }

    public int maxPartitionFactor(int[][] points) {
        this.points = points;
        n = points.length;
        if (n == 2) return 0;
        int lo = 0, hi = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                hi = Math.max(hi, dist(i, j));
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
