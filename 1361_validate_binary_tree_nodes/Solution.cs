// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

using System.Collections.Generic;
public class Solution {
    public bool ValidateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        var indeg = new int[n];
        foreach (int x in leftChild) if (x != -1 && ++indeg[x] > 1) return false;
        foreach (int x in rightChild) if (x != -1 && ++indeg[x] > 1) return false;
        var roots = new List<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) roots.Add(i);
        if (roots.Count != 1) return false;
        var seen = new HashSet<int>();
        var st = new Stack<int>(); st.Push(roots[0]);
        while (st.Count > 0) {
            int u = st.Pop();
            if (!seen.Add(u)) return false;
            if (leftChild[u] != -1) st.Push(leftChild[u]);
            if (rightChild[u] != -1) st.Push(rightChild[u]);
        }
        return seen.Count == n;
    }
}
