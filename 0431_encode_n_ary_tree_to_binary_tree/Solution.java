// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

import java.util.ArrayList;
import java.util.List;

class Node {
    public int val;
    public List<Node> children;

    public Node() {
        children = new ArrayList<>();
    }

    public Node(int val) {
        this.val = val;
        children = new ArrayList<>();
    }

    public Node(int val, List<Node> children) {
        this.val = val;
        this.children = children;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode encodeNaryTree(Node root) {
        if (root == null) {
            return null;
        }
        TreeNode binary = new TreeNode(root.val);
        if (root.children.isEmpty()) {
            return binary;
        }
        binary.left = encodeNaryTree(root.children.get(0));
        TreeNode sibling = binary.left;
        for (int i = 1; i < root.children.size(); i++) {
            sibling.right = encodeNaryTree(root.children.get(i));
            sibling = sibling.right;
        }
        return binary;
    }

    public Node decodeBinaryTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        Node node = new Node(root.val, new ArrayList<>());
        TreeNode current = root.left;
        while (current != null) {
            node.children.add(decodeBinaryTree(current));
            current = current.right;
        }
        return node;
    }
}
