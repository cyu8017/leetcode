// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

using System.Collections.Generic;

/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;
}
*/

public class Solution {
    public IList<int> Preorder(Node root) {
        var result = new List<int>();
        Dfs(root, result);
        return result;
    }

    private void Dfs(Node node, List<int> result) {
        if (node == null) return;
        result.Add(node.val);
        if (node.children != null) {
            foreach (Node child in node.children) Dfs(child, result);
        }
    }
}
