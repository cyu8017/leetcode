// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

using System.Collections.Generic;

public class Solution {
    public int[][] BuildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        int[] Topo(int[][] conds) {
            var g = new List<int>[k + 1];
            for (int i = 0; i <= k; i++) g[i] = new List<int>();
            int[] indeg = new int[k + 1];
            foreach (var c in conds) {
                g[c[0]].Add(c[1]);
                indeg[c[1]]++;
            }
            var q = new Queue<int>();
            for (int i = 1; i <= k; i++) if (indeg[i] == 0) q.Enqueue(i);
            var order = new List<int>();
            while (q.Count > 0) {
                int u = q.Dequeue();
                order.Add(u);
                foreach (int v in g[u]) if (--indeg[v] == 0) q.Enqueue(v);
            }
            if (order.Count != k) return null;
            return order.ToArray();
        }
        int[] rowOrder = Topo(rowConditions);
        int[] colOrder = Topo(colConditions);
        if (rowOrder == null || colOrder == null) return new int[0][];
        int[] rowPos = new int[k + 1], colPos = new int[k + 1];
        for (int i = 0; i < k; i++) {
            rowPos[rowOrder[i]] = i;
            colPos[colOrder[i]] = i;
        }
        var ans = new int[k][];
        for (int i = 0; i < k; i++) ans[i] = new int[k];
        for (int v = 1; v <= k; v++) ans[rowPos[v]][colPos[v]] = v;
        return ans;
    }
}
