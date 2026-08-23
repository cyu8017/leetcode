// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

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
    public Node InorderSuccessor(Node node) {
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
