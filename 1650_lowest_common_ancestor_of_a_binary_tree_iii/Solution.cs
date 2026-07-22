// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

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
    public Node LowestCommonAncestor(Node p, Node q) {
        Node a = p, b = q;
        while (a != b) {
            a = a != null ? a.parent : q;
            b = b != null ? b.parent : p;
        }
        return a;
    }
}
