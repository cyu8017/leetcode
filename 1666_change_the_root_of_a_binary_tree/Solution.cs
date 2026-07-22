// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

public class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
    public Node(int val = 0, Node left = null, Node right = null, Node parent = null) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.parent = parent;
    }
}

public class Solution {
    public Node FlipBinaryTree(Node root, Node leaf) {
        Node node = leaf;
        while (node != root) {
            Node parent = node.parent;
            if (parent.left == node) parent.left = null;
            else parent.right = null;
            Node originalLeft = node.left;
            node.left = parent;
            if (originalLeft != null) node.right = originalLeft;
            node = parent;
        }
        FixParent(leaf, null);
        return leaf;
    }

    private void FixParent(Node cur, Node parent) {
        if (cur == null) return;
        cur.parent = parent;
        FixParent(cur.left, cur);
        FixParent(cur.right, cur);
    }
}
