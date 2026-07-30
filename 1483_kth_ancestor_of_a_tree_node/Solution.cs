// LeetCode 1483 - Kth Ancestor Of A Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

using System.Collections.Generic;
public class TreeAncestor {
    List<int[]> up = new List<int[]>();
    public TreeAncestor(int n, int[] parent) {
        int width = 1; while ((1 << width) <= n) width++;
        up.Add((int[])parent.Clone());
        for (int b = 1; b < width; b++) {
            var prev = up[b - 1];
            var cur = new int[n];
            for (int i = 0; i < n; i++) cur[i] = prev[i] == -1 ? -1 : prev[prev[i]];
            up.Add(cur);
        }
    }
    public int GetKthAncestor(int node, int k) {
        int bit = 0;
        while (k > 0 && node != -1) {
            if ((k & 1) != 0) {
                if (bit >= up.Count) return -1;
                node = up[bit][node];
            }
            bit++; k >>= 1;
        }
        return node;
    }
}
