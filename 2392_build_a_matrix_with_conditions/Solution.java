// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        int[] rowOrder = topo(k, rowConditions);
        int[] colOrder = topo(k, colConditions);
        if (rowOrder == null || colOrder == null) return new int[0][];
        int[] rowPos = new int[k + 1], colPos = new int[k + 1];
        for (int i = 0; i < k; i++) {
            rowPos[rowOrder[i]] = i;
            colPos[colOrder[i]] = i;
        }
        int[][] ans = new int[k][k];
        for (int v = 1; v <= k; v++) ans[rowPos[v]][colPos[v]] = v;
        return ans;
    }

    private int[] topo(int k, int[][] conds) {
        List<Integer>[] g = new ArrayList[k + 1];
        for (int i = 0; i <= k; i++) g[i] = new ArrayList<>();
        int[] indeg = new int[k + 1];
        for (int[] c : conds) {
            g[c[0]].add(c[1]);
            indeg[c[1]]++;
        }
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 1; i <= k; i++) if (indeg[i] == 0) q.offer(i);
        int[] order = new int[k];
        int idx = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            order[idx++] = u;
            for (int v : g[u]) {
                if (--indeg[v] == 0) q.offer(v);
            }
        }
        if (idx != k) return null;
        return order;
    }
}
