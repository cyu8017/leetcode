// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

using System.Collections.Generic;

public class Node {
    public int val;
    public IList<Node> children;
    public Node() {
        children = new List<Node>();
    }
    public Node(int val, IList<Node> children = null) {
        this.val = val;
        this.children = children ?? new List<Node>();
    }
}

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public TreeNode EncodeNaryTree(Node root) {
        if (root == null) {
            return null;
        }
        TreeNode binary = new TreeNode(root.val);
        if (root.children.Count == 0) {
            return binary;
        }
        binary.left = EncodeNaryTree(root.children[0]);
        TreeNode sibling = binary.left;
        for (int i = 1; i < root.children.Count; i++) {
            sibling.right = EncodeNaryTree(root.children[i]);
            sibling = sibling.right;
        }
        return binary;
    }

    public Node DecodeBinaryTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        Node node = new Node(root.val, new List<Node>());
        TreeNode current = root.left;
        while (current != null) {
            node.children.Add(DecodeBinaryTree(current));
            current = current.right;
        }
        return node;
    }
}
