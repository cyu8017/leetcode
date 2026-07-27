// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;

    public Node() {}

    public Node(int val) {
        this.val = val;
    }
}

class Solution {
    public Node flipBinaryTree(Node root, Node leaf) {
        Node node = leaf;
        while (node != root) {
            Node parent = node.parent;
            if (parent.left == node) {
                parent.left = null;
            } else {
                parent.right = null;
            }
            Node originalLeft = node.left;
            node.left = parent;
            if (originalLeft != null) {
                node.right = originalLeft;
            }
            node = parent;
        }
        fixParent(leaf, null);
        return leaf;
    }

    private void fixParent(Node cur, Node parent) {
        if (cur == null) {
            return;
        }
        cur.parent = parent;
        fixParent(cur.left, cur);
        fixParent(cur.right, cur);
    }
}
