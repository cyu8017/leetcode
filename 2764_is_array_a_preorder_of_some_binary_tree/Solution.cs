// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

using System.Collections.Generic;

public class Solution {
    public bool IsPreorder(IList<IList<int>> nodes) {
        if (nodes.Count == 0) return true;
        var stack = new List<int>();
        stack.Add(nodes[0][0]);
        for (int i = 1; i < nodes.Count; i++) {
            int id = nodes[i][0], parent = nodes[i][1];
            while (stack.Count > 0 && stack[^1] != parent) stack.RemoveAt(stack.Count - 1);
            if (stack.Count == 0) return false;
            stack.Add(id);
        }
        return true;
    }
}
