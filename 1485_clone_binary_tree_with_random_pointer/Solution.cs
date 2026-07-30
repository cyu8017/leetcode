// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

using System.Collections.Generic;
public class Node {
    public int val; public Node left; public Node right; public Node random;
    public Node(int val = 0) { this.val = val; }
}
public class Solution {
    Dictionary<Node, Node> copies = new Dictionary<Node, Node>();
    public Node CopyRandomBinaryTree(Node root) {
        if (root == null) return null;
        if (!copies.ContainsKey(root)) {
            copies[root] = new Node(root.val);
            copies[root].left = CopyRandomBinaryTree(root.left);
            copies[root].right = CopyRandomBinaryTree(root.right);
            copies[root].random = CopyRandomBinaryTree(root.random);
        }
        return copies[root];
    }
}
