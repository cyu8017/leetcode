// LeetCode 1483 - Kth Ancestor Of A Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

import java.util.*;

class TreeAncestor {
    List<int[]> up = new ArrayList<>();
    public TreeAncestor(int n, int[] parent) {
        int width = 1; while ((1 << width) <= n) width++;
        up.add((int[])parent.Clone());
        for (int b = 1; b < width; b++) {
            var prev = up[b - 1];
            var cur = new int[n];
            for (int i = 0; i < n; i++) cur[i] = prev[i] == -1 ? -1 : prev[prev[i]];
            up.add(cur);
        }
    }
    public int getKthAncestor(int node, int k) {
        int bit = 0;
        while (k > 0 && node != -1) {
            if ((k & 1) != 0) {
                if (bit >= up.size()) return -1;
                node = up[bit][node];
            }
            bit++; k >>= 1;
        }
        return node;
    }
}
