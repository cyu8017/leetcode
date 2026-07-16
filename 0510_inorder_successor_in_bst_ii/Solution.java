// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

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
    public Node inorderSuccessor(Node node) {
        if (node.right != null) {
            Node current = node.right;
            while (current.left != null) {
                current = current.left;
            }
            return current;
        }
        Node current = node;
        while (current.parent != null && current == current.parent.right) {
            current = current.parent;
        }
        return current.parent;
    }
}
