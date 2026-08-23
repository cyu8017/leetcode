// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        int lo = 1, hi = 1000001, ans = -1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(n, edges, mid)) {
                ans = mid;
                hi = mid;
            } else lo = mid + 1;
        }
        return ans;
    }

    private boolean ok(int n, int[][] edges, int mid) {
        List<List<Integer>> g = new ArrayList<>();
        for (int i = 0; i < n; i++) g.add(new ArrayList<>());
        for (int[] e : edges) {
            if (e[2] <= mid) g.get(e[1]).add(e[0]);
        }
        boolean[] vis = new boolean[n];
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(0);
        vis[0] = true;
        int cnt = 1;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g.get(u)) {
                if (!vis[v]) {
                    vis[v] = true;
                    cnt++;
                    q.offer(v);
                }
            }
        }
        return cnt == n;
    }
}
