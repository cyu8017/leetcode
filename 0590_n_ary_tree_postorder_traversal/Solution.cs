// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

using System.Collections.Generic;

/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;
}
*/

public class Solution {
    public IList<int> Postorder(Node root) {
        var result = new List<int>();
        Dfs(root, result);
        return result;
    }

    private void Dfs(Node node, List<int> result) {
        if (node == null) return;
        if (node.children != null) {
            foreach (Node child in node.children) Dfs(child, result);
        }
        result.Add(node.val);
    }
}
