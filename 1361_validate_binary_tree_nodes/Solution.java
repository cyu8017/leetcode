// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

import java.util.*;

class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        var indeg = new int[n];
        for (int x : leftChild) if (x != -1 && ++indeg[x] > 1) return false;
        for (int x : rightChild) if (x != -1 && ++indeg[x] > 1) return false;
        var roots = new ArrayList<>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) roots.add(i);
        if (roots.size() != 1) return false;
        var seen = new HashSet<>();
        var st = new ArrayDeque<>(); st.push(roots[0]);
        while (st.size() > 0) {
            int u = st.pop();
            if (!seen.add(u)) return false;
            if (leftChild[u] != -1) st.push(leftChild[u]);
            if (rightChild[u] != -1) st.push(rightChild[u]);
        }
        return seen.size() == n;
    }
}
