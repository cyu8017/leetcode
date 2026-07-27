// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

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
    public Node lowestCommonAncestor(Node p, Node q) {
        Node a = p;
        Node b = q;
        while (a != b) {
            a = a != null ? a.parent : q;
            b = b != null ? b.parent : p;
        }
        return a;
    }
}
